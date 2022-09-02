ENERGYSITE_SOLAR = {
    "energy_site_id": 12345,
    "resource_type": "solar",
    "id": "313dbc37-555c-45b1-83aa-62a4ef9ff7ac",
    "asset_site_id": "12345",
    "solar_power": 2260,
    "solar_type": "pv_panel",
    "storm_mode_enabled": None,
    "powerwall_onboarding_settings_set": None,
    "sync_grid_alert_enabled": False,
    "breaker_alert_enabled": False,
    "components": {
        "battery": False,
        "solar": True,
        "solar_type": "pv_panel",
        "grid": True,
        "load_meter": True,
        "market_type": "residential",
    },
}

ENERGYSITE_BATTERY = {
    "energy_site_id": 67890,
    "resource_type": "battery",
    "site_name": "Battery Home",
    "id": "313dbc37-555c-45b1-83aa-62a4ef9ff7ab",
    "asset_site_id": "67890",
    "solar_power": 3456,
    "solar_type": "pv_panel",
    "storm_mode_enabled": None,
    "powerwall_onboarding_settings_set": None,
    "sync_grid_alert_enabled": False,
    "breaker_alert_enabled": False,
    "components": {
        "battery": True,
        "solar": True,
        "solar_type": "pv_panel",
        "grid": True,
        "load_meter": True,
        "market_type": "residential",
    },
}

SITE_DATA = {
    "solar_power": 7720,
    "energy_left": 0,
    "total_pack_energy": 1,
    "percentage_charged": 0,
    "battery_power": 0,
    "load_power": 4517.14990234375,
    "grid_status": "Unknown",
    "grid_services_active": False,
    "grid_power": -3202.85009765625,
    "grid_services_power": 0,
    "generator_power": 0,
    "island_status": "island_status_unknown",
    "storm_mode_active": False,
    "timestamp": "2022-07-28T17:11:27Z",
    "wall_connectors": None,
}

BATTERY_DATA = {
    "energy_site_id": 67890,
    "resource_type": "battery",
    "site_name": "My Battery Home",
    "id": "XXX",
    "gateway_id": "XXX",
    "asset_site_id": "XXX",
    "energy_left": 12650.052631578948,
    "total_pack_energy": 14069,
    "percentage_charged": 20.360603000037408,
    "solar": True,
    "solar_type": "pv_panel",
    "battery": True,
    "grid": True,
    "backup": True,
    "gateway": "teg",
    "load_meter": True,
    "tou_capable": True,
    "storm_mode_capable": True,
    "flex_energy_request_capable": False,
    "car_charging_data_supported": False,
    "off_grid_vehicle_charging_reserve_supported": False,
    "vehicle_charging_performance_view_enabled": False,
    "vehicle_charging_solar_offset_view_enabled": False,
    "battery_solar_offset_view_enabled": True,
    "solar_value_enabled": True,
    "energy_value_header": "Energy Value",
    "energy_value_subheader": "Estimated Value",
    "show_grid_import_battery_source_cards": True,
    "backup_time_remaining_enabled": True,
    "rate_plan_manager_supported": True,
    "battery_type": "ac_powerwall",
    "configurable": False,
    "grid_services_enabled": False,
    "customer_preferred_export_rule": "battery_ok",
    "net_meter_mode": "battery_ok",
    "grid_status": "Active",
    "backup_reserve_percent": 100,
    "default_real_mode": "backup",
    "operation": "backup",
    "timestamp": "2022-08-16T15:23:24+10:00",
    "load_power": 329,
    "solar_power": 709,
    "grid_power": 2930,
    "battery_power": -3310,
    "generator_power": 0,
}
