import voluptuous as vol
from homeassistant import config_entries
from homeassistant.const import CONF_PORT
from .const import DOMAIN

CONF_BAUDRATE = "baudrate"

class HdmiMatrixConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        if user_input:
            return self.async_create_entry(title="HDMI Matrix", data=user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required(CONF_PORT, default="/dev/ttyUSB0"): str,
                vol.Optional(CONF_BAUDRATE, default=19200): int
            })
        )
