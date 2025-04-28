from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType
from .const import DOMAIN

async def async_setup(hass: HomeAssistant, config: ConfigType):
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    hass.data.setdefault(DOMAIN, {})
    from .rs232_matrix import HdmiMatrix
    matrix = HdmiMatrix(entry.data["port"], entry.data["baudrate"])
    hass.data[DOMAIN][entry.entry_id] = matrix

    # Dienst zur Eingang-Umschaltung registrieren
    async def handle_switch_input(call):
        output = call.data.get("output")
        input_ = call.data.get("input")
        matrix.switch(output, input_)

    hass.services.async_register(
        DOMAIN,
        "switch_input",
        handle_switch_input
    )

    # WICHTIG: Korrekt awaiten und mehrere Plattformen unterstützen
    await hass.config_entries.async_forward_entry_setups(entry, ["select"])

    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    await hass.config_entries.async_forward_entry_unload(entry, "select")
    hass.data[DOMAIN].pop(entry.entry_id)
    return True
