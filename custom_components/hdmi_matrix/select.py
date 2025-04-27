from homeassistant.components.select import SelectEntity
from homeassistant.core import callback
from .const import DOMAIN, OUTPUTS, INPUTS

async def async_setup_entry(hass, entry, async_add_entities):
    matrix = hass.data[DOMAIN][entry.entry_id]
    entities = [HdmiMatrixSelect(matrix, output_id) for output_id in OUTPUTS]
    async_add_entities(entities)

class HdmiMatrixSelect(SelectEntity):
    def __init__(self, matrix, output_id):
        self._matrix = matrix
        self._output_id = output_id
        self._attr_name = f"HDMI Output {OUTPUTS[output_id]}"
        self._attr_options = list(INPUTS.values())
        self._attr_unique_id = f"hdmi_output_{OUTPUTS[output_id].lower()}"
        self._attr_icon = "mdi:video-input-hdmi"
        self._attr_current_option = None

    async def async_update(self):
        input_id = self._matrix.get_status(self._output_id)
        if input_id in INPUTS:
            self._attr_current_option = INPUTS[input_id]

    async def async_select_option(self, option: str):
        reverse_map = {v: k for k, v in INPUTS.items()}
        input_id = reverse_map.get(option)
        if input_id:
            self._matrix.switch(self._output_id, input_id)
            self._attr_current_option = option