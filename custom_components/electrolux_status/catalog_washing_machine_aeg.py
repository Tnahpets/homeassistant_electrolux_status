"""Defined catalog of entities for AEG washing machine devices."""

from homeassistant.components.binary_sensor import BinarySensorDeviceClass
from homeassistant.components.button import ButtonDeviceClass
from homeassistant.const import EntityCategory

from .model import ElectroluxDevice

# AEG LR8 Series Washing Machines (e.g., LR8Munster)
LR8MUNSTER = {
    # Door States
    "doorState": ElectroluxDevice(
        device_class=BinarySensorDeviceClass.DOOR,
        unit=None,
        entity_category=None,
        entity_icon="mdi:door",
        friendly_name="Door State",
    ),
    "doorLock": ElectroluxDevice(
        device_class=BinarySensorDeviceClass.LOCK,
        unit=None,
        entity_category=None,
        entity_icon="mdi:lock",
        friendly_name="Door Lock",
        state_invert=True,  # Inverts the state - locked shows as True
    ),
    # Execute Commands - Button functionality
    "executeCommand/START": ElectroluxDevice(
        device_class=ButtonDeviceClass.RESTART,
        unit=None,
        entity_category=None,
        entity_icon="mdi:play",
        friendly_name="Start Wash",
    ),
    "executeCommand/PAUSE": ElectroluxDevice(
        device_class=None,
        unit=None,
        entity_category=None,
        entity_icon="mdi:pause",
        friendly_name="Pause Wash",
    ),
    "executeCommand/RESUME": ElectroluxDevice(
        device_class=None,
        unit=None,
        entity_category=None,
        entity_icon="mdi:play-pause",
        friendly_name="Resume Wash",
    ),
    "executeCommand/STOPRESET": ElectroluxDevice(
        device_class=None,
        unit=None,
        entity_category=None,
        entity_icon="mdi:stop",
        friendly_name="Stop Wash",
    ),
}