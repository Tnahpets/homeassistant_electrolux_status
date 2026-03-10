"""Defined catalog of entities for AEG washing machine devices."""

from homeassistant.components.binary_sensor import BinarySensorDeviceClass
from homeassistant.components.button import ButtonDeviceClass
from homeassistant.components.sensor import SensorDeviceClass
from homeassistant.const import PERCENTAGE, EntityCategory, UnitOfTime, UnitOfVolume

from .model import ElectroluxDevice

# AEG LR8 Series Washing Machines (e.g., LR8Munster)
LR8MUNSTER = {
    # Door States
    "doorState": ElectroluxDevice(
        device_class=BinarySensorDeviceClass.DOOR,
        unit=None,
        entity_category=None,
        entity_icon="mdi:door",
        translation_key="door_state",
    ),
    "doorLock": ElectroluxDevice(
        device_class=BinarySensorDeviceClass.LOCK,
        unit=None,
        entity_category=None,
        entity_icon="mdi:lock",
        translation_key="door_lock",
        state_invert=True,  # Inverts the state - locked shows as True
    ),
    # Cycle Progress
    "cyclePhase": ElectroluxDevice(
        device_class=None,
        unit=None,
        entity_category=None,
        entity_icon="mdi:washing-machine",
        translation_key="cycle_phase",
    ),
    "cycleSubPhase": ElectroluxDevice(
        device_class=None,
        unit=None,
        entity_category=None,
        entity_icon="mdi:washing-machine",
        translation_key="cycle_sub_phase",
    ),
    "timeToEnd": ElectroluxDevice(
        device_class=SensorDeviceClass.DURATION,
        unit=UnitOfTime.SECONDS,
        entity_category=None,
        entity_icon="mdi:timer-sand",
        translation_key="time_to_end",
    ),
    # Resource Usage
    "fCMiscellaneousState/waterUsage": ElectroluxDevice(
        device_class=UnitOfVolume.LITERS,
        unit=UnitOfVolume.LITERS,
        entity_category=None,
        entity_icon="mdi:water",
        translation_key="water_usage",
    ),
    # Auto-Dosing System
    "fCMiscellaneousState/adTankADetLoaded": ElectroluxDevice(
        device_class=None,
        unit=PERCENTAGE,
        entity_category=None,
        entity_icon="mdi:cup-water",
        translation_key="autodose_tank_a_level",
    ),
    "fCMiscellaneousState/adTankBSoftLoaded": ElectroluxDevice(
        device_class=None,
        unit=PERCENTAGE,
        entity_category=None,
        entity_icon="mdi:cup-water",
        translation_key="autodose_tank_b_level",
    ),
    "fCMiscellaneousState/tankAReserve": ElectroluxDevice(
        device_class=BinarySensorDeviceClass.PROBLEM,
        unit=None,
        entity_category=EntityCategory.DIAGNOSTIC,
        entity_icon="mdi:tray-alert",
        translation_key="autodose_tank_a_low",
    ),
    "fCMiscellaneousState/tankBReserve": ElectroluxDevice(
        device_class=BinarySensorDeviceClass.PROBLEM,
        unit=None,
        entity_category=EntityCategory.DIAGNOSTIC,
        entity_icon="mdi:tray-alert",
        translation_key="autodose_tank_b_low",
    ),
    "userSelections/adTankASel": ElectroluxDevice(
        device_class=None,
        unit=None,
        entity_category=EntityCategory.CONFIG,
        entity_icon="mdi:cog",
        translation_key="autodose_tank_a_setting",
    ),
    "userSelections/adTankBSel": ElectroluxDevice(
        device_class=None,
        unit=None,
        entity_category=EntityCategory.CONFIG,
        entity_icon="mdi:cog",
        translation_key="autodose_tank_b_setting",
    ),
    # Maintenance and Diagnostics
    "totalCycleCounter": ElectroluxDevice(
        device_class=None,
        unit="cycles",
        entity_category=EntityCategory.DIAGNOSTIC,
        entity_icon="mdi:counter",
        translation_key="total_cycle_count",
    ),
    "totalWashingTime": ElectroluxDevice(
        device_class=SensorDeviceClass.DURATION,
        unit=UnitOfTime.SECONDS,
        entity_category=EntityCategory.DIAGNOSTIC,
        entity_icon="mdi:clock-outline",
        translation_key="total_washing_time",
    ),
    "applianceTotalWorkingTime": ElectroluxDevice(
        device_class=SensorDeviceClass.DURATION,
        unit=UnitOfTime.SECONDS,
        entity_category=EntityCategory.DIAGNOSTIC,
        entity_icon="mdi:clock-check-outline",
        translation_key="total_working_time",
    ),
    "fcOptisenseLoadWeight": ElectroluxDevice(
        device_class=None,
        unit="g",
        entity_category=None,
        entity_icon="mdi:weight-kilogram",
        translation_key="measured_load_weight",
    ),
    # Execute Commands - Button functionality
    "executeCommand/START": ElectroluxDevice(
        device_class=ButtonDeviceClass.RESTART,
        unit=None,
        entity_category=None,
        entity_icon="mdi:play",
        translation_key="start_wash",
    ),
    "executeCommand/PAUSE": ElectroluxDevice(
        device_class=None,
        unit=None,
        entity_category=None,
        entity_icon="mdi:pause",
        translation_key="pause_wash",
    ),
    "executeCommand/RESUME": ElectroluxDevice(
        device_class=None,
        unit=None,
        entity_category=None,
        entity_icon="mdi:play-pause",
        translation_key="resume_wash",
    ),
    "executeCommand/STOPRESET": ElectroluxDevice(
        device_class=None,
        unit=None,
        entity_category=None,
        entity_icon="mdi:stop",
        translation_key="stop_wash",
    ),
    # Additional Status Information
    "applianceState": ElectroluxDevice(
        device_class=None,
        unit=None,
        entity_category=None,
        entity_icon="mdi:information-outline",
        translation_key="appliance_state",
    ),
    "washingNominalLoadWeight": ElectroluxDevice(
        device_class=None,
        unit="g",
        entity_category=EntityCategory.DIAGNOSTIC,
        entity_icon="mdi:weight-kilogram",
        translation_key="nominal_load_weight",
    ),
    "waterHardness": ElectroluxDevice(
        device_class=None,
        unit=None,
        entity_category=EntityCategory.CONFIG,
        entity_icon="mdi:water-opacity",
        translation_key="water_hardness",
    ),
    "uiLockMode": ElectroluxDevice(
        device_class=BinarySensorDeviceClass.LOCK,
        unit=None,
        entity_category=EntityCategory.CONFIG,
        entity_icon="mdi:lock-outline",
        translation_key="ui_lock",
    ),
    "remoteControl": ElectroluxDevice(
        device_class=None,
        unit=None,
        entity_category=EntityCategory.DIAGNOSTIC,
        entity_icon="mdi:remote",
        translation_key="remote_control_status",
    ),
    # AutoDosing Configuration
    "autoDosing/adTankAConfiguration": ElectroluxDevice(
        device_class=None,
        unit=None,
        entity_category=EntityCategory.CONFIG,
        entity_icon="mdi:cog",
        translation_key="autodose_tank_a_config",
    ),
    "autoDosing/adTankBConfiguration": ElectroluxDevice(
        device_class=None,
        unit=None,
        entity_category=EntityCategory.CONFIG,
        entity_icon="mdi:cog",
        translation_key="autodose_tank_b_config",
    ),
    "autoDosing/adTankADetStandardDose": ElectroluxDevice(
        device_class=None,
        unit="ml",
        entity_category=EntityCategory.CONFIG,
        entity_icon="mdi:flask-outline",
        translation_key="autodose_tank_a_std_dose",
    ),
    "autoDosing/adTankBSoftStandardDose": ElectroluxDevice(
        device_class=None,
        unit="ml",
        entity_category=EntityCategory.CONFIG,
        entity_icon="mdi:flask-outline",
        translation_key="autodose_tank_b_std_dose",
    ),
    # User Selections
    "userSelections/analogTemperature": ElectroluxDevice(
        device_class=None,
        unit=None,
        entity_category=None,
        entity_icon="mdi:thermometer",
        translation_key="selected_temperature",
    ),
    "userSelections/analogSpinSpeed": ElectroluxDevice(
        device_class=None,
        unit=None,
        entity_category=None,
        entity_icon="mdi:rotate-right",
        translation_key="selected_spin_speed",
    ),
    "userSelections/timeManagerLevel": ElectroluxDevice(
        device_class=None,
        unit=None,
        entity_category=None,
        entity_icon="mdi:clock-fast",
        translation_key="time_manager_level",
    ),
    "userSelections/steamValue": ElectroluxDevice(
        device_class=None,
        unit=None,
        entity_category=None,
        entity_icon="mdi:pot-steam",
        translation_key="steam_value",
    ),
    "userSelections/programUID": ElectroluxDevice(
        device_class=None,
        unit=None,
        entity_category=None,
        entity_icon="mdi:application-settings-outline",
        translation_key="program_uid",
    ),
}