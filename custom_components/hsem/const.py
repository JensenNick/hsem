DOMAIN = "hsem"
NAME = "Huawei Solar Energy Management"
ICON = "mdi:power"

DEFAULT_HSEM_ENERGI_DATA_SERVICE_IMPORT = "sensor.energi_data_service"
DEFAULT_HSEM_ENERGI_DATA_SERVICE_EXPORT = "sensor.energi_data_service_produktion"
DEFAULT_HSEM_HUAWEI_SOLAR_BATTERIES_WORKING_MODE = "select.battery_working_mode"
DEFAULT_HSEM_HUAWEI_SOLAR_BATTERIES_STATE_OF_CAPACITY = (
    "sensor.battery_state_of_capacity"
)
DEFAULT_HSEM_HUAWEI_SOLAR_INVERTER_ACTIVE_POWER_CONTROL = (
    "sensor.inverter_active_power_control"
)
DEFAULT_HSEM_HOUSE_CONSUMPTION_POWER = "sensor.power_house_load"
DEFAULT_HSEM_SOLAR_PRODUCTION_POWER = "sensor.power_inverter_input_total"
DEFAULT_HSEM_SOLCAST_PV_FORECAST_FORECAST_TODAY = (
    "sensor.solcast_pv_forecast_forecast_today"
)
DEFAULT_HSEM_SOLCAST_PV_FORECAST_FORECAST_TOMORROW = (
    "sensor.solcast_pv_forecast_forecast_tomorrow"
)
DEFAULT_HSEM_MORNING_ENERGY_NEED = 1.5
DEFAULT_HSEM_BATTERY_MAX_CAPACITY = 10
DEFAULT_HSEM_EV_CHARGER_STATUS = "sensor.go_echarger_is_charging"

DEFAULT_HSEM_IMPORT_SENSOR_TOU_MODES = ["00:00-23:59/1234567/+"]
DEFAULT_HSEM_EV_CHARGER_TOU_MODES = ["00:00-00:01/1234567/+"]
DEFAULT_HSEM_DEFAULT_TOU_MODES = [
            "00:01-05:59/1234567/+",
            "06:00-10:00/1234567/-",
            "17:00-23:59/1234567/-",
        ]

DEFAULT_HSEM_MONTHS_WINTER_SPRING = [1, 2, 3, 4, 9, 10, 11, 12]
DEFAULT_HSEM_MONTHS_SUMMER = [5, 6, 7, 8]
