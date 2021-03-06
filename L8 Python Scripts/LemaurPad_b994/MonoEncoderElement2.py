# emacs-mode: -*- python-*-
import Live
from _Framework.EncoderElement import EncoderElement
from _Framework.InputControlElement import InputControlElement
from _Framework.NotifyingControlElement import NotifyingControlElement

MIDI_NOTE_TYPE = 0
MIDI_CC_TYPE = 1
MIDI_PB_TYPE = 2
MIDI_MSG_TYPES = (MIDI_NOTE_TYPE,
 MIDI_CC_TYPE,
 MIDI_PB_TYPE)
MIDI_NOTE_ON_STATUS = 144
MIDI_NOTE_OFF_STATUS = 128
MIDI_CC_STATUS = 176
MIDI_PB_STATUS = 224

class MonoEncoderElement2(EncoderElement):
	__module__ = __name__
	__doc__ = ' Class representing a slider on the controller '

	def __init__(self, msg_type, channel, identifier, map_mode, name, num, osc, osc_parameter, osc_name, script):
		EncoderElement.__init__(self, msg_type, channel, identifier, map_mode=Live.MidiMap.MapMode.absolute)
		self.name = name
		self.num = num
		self._parameter = None
		self._script = script
		self.osc = osc
		self.osc_parameter = osc_parameter
		self.osc_name = osc_name
		self._timer = 0
		self._is_enabled = True
		self._report_input = True
		self._report_output = True
		self._paramter_lcd_name = ' '
		self._parameter_last_value = None
		self._mapped_to_midi_velocity = False
		self._mapping_feedback_delay = 0
		self._threshold = 0
		self._script._monobridge._send_osc(self.osc, 0, True)

	def disconnect(self):
		self.remove_parameter_listener(self._parameter)
		EncoderElement.disconnect(self)
		
	def connect_to(self, parameter):
		assert (parameter != None)
		assert isinstance(parameter, Live.DeviceParameter.DeviceParameter)
		self._mapped_to_midi_velocity = False
		assignment = parameter
		if(str(parameter.name) == str('Track Volume')):		#checks to see if parameter is track volume
			if(parameter.canonical_parent.canonical_parent.has_audio_output is False):		#checks to see if track has audio output
				if(len(parameter.canonical_parent.canonical_parent.devices) > 0):
					if(str(parameter.canonical_parent.canonical_parent.devices[0].class_name)==str('MidiVelocity')):	#if not, looks for velicty as first plugin
						assignment = parameter.canonical_parent.canonical_parent.devices[0].parameters[6]				#if found, assigns fader to its 'outhi' parameter
						self._mapped_to_midi_velocity = True
		self._parameter_to_map_to = assignment
		self.add_parameter_listener(self._parameter_to_map_to)

	def set_enabled(self, enabled):
		self._is_enabled = enabled

	def set_value(self, value):
		if(self._parameter_to_map_to != None):
			newval = float(value * (self._parameter_to_map_to.max - self._parameter_to_map_to.min)) + self._parameter_to_map_to.min
			self._parameter_to_map_to.value = newval
			self._timer = self._script._timer
			#self._script.log_message(str(value) + str('@') + str(self._script._timer) + ' ' + str(self._timer))
			return [value, str(self.mapped_parameter())]
		else:
			self.receive_value(int(value*127))
			self._timer = self._script._timer
			#self._script.log_message(str(value) + str('@') + str(self._script._timer))
	
	def release_parameter(self):
		if(self._parameter_to_map_to != None):
			self.remove_parameter_listener(self._parameter_to_map_to)
			self._parameter_to_map_to = None

	def install_connections(self):	#this override has to be here so that translation will happen when buttons are disabled
		if self._is_enabled:
			EncoderElement.install_connections(self)
		elif ((self._msg_channel != self._original_channel) or (self._msg_identifier != self._original_identifier)):
			self._install_translation(self._msg_type, self._original_identifier, self._original_channel, self._msg_identifier, self._msg_channel)

	def forward_parameter_value(self):
		if(not (type(self._parameter) is type(None))):
			#new_value=int(((self._parameter.value - self._parameter.min) / (self._parameter.max - self._parameter.min))  * 127)
			try:
				parameter = str(self.mapped_parameter())
			except:
				parameter = ' '
			if(parameter!=self._parameter_last_value):
				try:
					self._parameter_last_value = str(self.mapped_parameter())
				except:
					self._parameter_last_value = ' '
				self._script._monobridge._send_osc(self.osc_parameter, self._script.generate_strip_string(self._parameter_last_value), True, True)
				if (self._timer  + self._threshold) < self._script._timer:
					new_value=float((self._parameter.value - self._parameter.min) / (self._parameter.max - self._parameter.min))
					self._script._monobridge._send_osc(self.osc, new_value)
					#self._script.log_message(str(self._timer) + ' ' + str(self._script._timer) + ' ' + str(new_value))

	def forward_parameter_name(self):
		if(not (type(self._parameter) is type(None))):
			parameter = self._parameter
			if parameter:
				if isinstance(parameter, Live.DeviceParameter.DeviceParameter):
					if str(parameter.original_name) == 'Track Volume' or self._mapped_to_midi_velocity is True:
						self._parameter_lcd_name = str(parameter.canonical_parent.canonical_parent.name)
					elif str(parameter.original_name) == 'Track Panning':
						self._parameter_lcd_name = 'Pan'
					else:
						self._parameter_lcd_name = str(parameter.name)
				self._script._monobridge._send_osc(self.osc_name, self._script.generate_strip_string(self._parameter_lcd_name), False, True)	



	def add_parameter_listener(self, parameter):
		self._parameter = parameter
		if parameter:
			if isinstance(parameter, Live.DeviceParameter.DeviceParameter):
				if str(parameter.original_name) == 'Track Volume' or self._mapped_to_midi_velocity is True:
					self._parameter_lcd_name = str(parameter.canonical_parent.canonical_parent.name)
					cbb = lambda: self.forward_parameter_name()
					parameter.canonical_parent.canonical_parent.add_name_listener(cbb)
				elif str(parameter.original_name) == 'Track Panning':
					self._parameter_lcd_name = 'Pan'
				else:
					self._parameter_lcd_name = str(parameter.name)
			#self._last_value(int(((self._parameter.value - self._parameter.min) / (self._parameter.max - self._parameter.min))  * 127))
			try:
				self._parameter_last_value = str(self.mapped_parameter())
			except:
				self._parameter_last_value = ' '
			self._script._monobridge._send_osc(self.osc_name, self._script.generate_strip_string(self._parameter_lcd_name), False, True)
			self._script._monobridge._send_osc(self.osc_parameter, self._script.generate_strip_string(self._parameter_last_value), False, True)
			new_value=float((self._parameter.value - self._parameter.min) / (self._parameter.max - self._parameter.min))
			self._script._monobridge._send_osc(self.osc, new_value)
			cb = lambda: self.forward_parameter_value()
			parameter.add_value_listener(cb)



	def remove_parameter_listener(self, parameter):
		self._parameter = None
		#self._script.log_message('remove_parameter_listener ' + str(parameter.name + str(self.name)))
		if parameter:
			cb = lambda: self.forward_parameter_value()
			cbb = lambda: self.forward_parameter_name()
			if(parameter.value_has_listener is True):
				parameter.remove_value_listener(cb)
			if isinstance(parameter, Live.DeviceParameter.DeviceParameter):
				if str(parameter.original_name) == 'Track Volume' or self._mapped_to_midi_velocity is True:
					if(parameter.canonical_parent.canonical_parent.name_has_listener is True):
						parameter.canonical_parent.canonical_parent.remove_name_listener(cbb)
			self._parameter_lcd_name = ' '
			self._parameter_last_value = ' '
			#self._script.notification_to_bridge(' ', ' ', self)
			self._script._monobridge._send_osc(self.osc, 0)
			self._script._monobridge._send_osc(self.osc_name, '`_', False, True)
			self._script._monobridge._send_osc(self.osc_parameter, '`_', False, True)

#	def receive_value(self, value):
#		self._script.log_message(str(self._name) + str(value))
#		InputControlElement.receive_value(self, value)
	
#	def send_midi(self, message):
#		assert (message != None)
#		assert isinstance(message, tuple)
#		#self._send_midi(message)
#		self._script.log_message('encoder' + str(message))
#		if(message[2]!=self._last_sent_value):
#			self._script._monobridge._send_osc(self.osc, message[2]/127)
#	def send_midi(self, message):
#		assert (message != None)
#		assert isinstance(message, tuple)
#		self._send_midi(message)
		#self._script.log_message(str(message))
		#if(message[2]!=self._listener._mode_index):
		#	self._script.notification_to_bridge(int(message[2]), self)

