import hashlib
import logging

from .const import (
    DOMAIN,
)

from .custom_sensors.export_sensor import ExportSensor

_LOGGER = logging.getLogger(__name__)

def generate_md5_hash(input_sensor):
    """Generate an MD5 hash based on the input sensor's name."""
    return hashlib.md5(input_sensor.encode("utf-8")).hexdigest()

def get_config_value(config_entry, key, default_value):
    """Get the configuration value from options or fall back to the initial data."""
    return config_entry.options.get(key, config_entry.data.get(key, default_value))


async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up HSEM sensors from a config entry."""
    config = config_entry.data

    # Extract configuration parameters
    hsem_energi_data_service_import = config.get("hsem_energi_data_service_import")
    hsem_energi_data_service_export = config.get("hsem_energi_data_service_export")

    # Create the export from the input from hsem_energi_data_service_export
    export_sensor = ExportSensor(
        hsem_energi_data_service_export, generate_md5_hash(hsem_energi_data_service_export), config_entry
    )

    # Add sensors to Home Assistant
    async_add_entities(
        [
            export_sensor,
        ]
    )

    # Store reference to the platform to handle unloads later
    if DOMAIN not in hass.data:
        hass.data[DOMAIN] = {}
    hass.data[DOMAIN][config_entry.entry_id] = async_add_entities


async def async_unload_entry(hass, entry):
    """Handle unloading of an entry."""
    platform = hass.data[DOMAIN].get(entry.entry_id)
    if platform:
        return await platform.async_remove_entry(entry)
    return False
