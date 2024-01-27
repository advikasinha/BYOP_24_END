import winreg
import subprocess

def get_supported_battery_plans():
    battery_plans = {}

    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Power\User\PowerSchemes") as key:
        subkey_index = 0
        while True:
            try:
                subkey_name = winreg.EnumKey(key, subkey_index)
                subkey_path = rf"SYSTEM\CurrentControlSet\Control\Power\User\PowerSchemes\{subkey_name}"

                with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, subkey_path) as subkey:
                    friendly_name, _ = winreg.QueryValueEx(subkey, "FriendlyName")
                    
                    #extracting just the battery plan name from the friendly name
                plan_name = friendly_name.split(",")[-1].strip()
                battery_plans[subkey_name] = plan_name
                subkey_index += 1

            except FileNotFoundError:
                break
            except Exception as e:
                break

    return battery_plans



def set_active_power_plan(plan_id):
    try:
        # Set the active power plan using powercfg command-line utility
        subprocess.run(["powercfg", "/setactive", plan_id], check=True)

        return True
    except subprocess.CalledProcessError as e:
        print(f"Error setting active power plan: {e}")
        return False

if __name__ == "__main__":

    supported_battery_plans = get_supported_battery_plans()

    if supported_battery_plans:
        print("Supported Battery Plans:")
        for plan_id, plan_name in supported_battery_plans.items():
            print(f"{plan_id}: {plan_name}")
    else:
        print("Unable to retrieve supported battery plans.")

    desired_power_plan_id = "381b4222-f694-41f0-9685-ff5bb260df2e"
    friendly_name= supported_battery_plans[desired_power_plan_id]


    if set_active_power_plan(desired_power_plan_id):
        print(f"Successfully set the active power plan to: {friendly_name}")
    else:
        print("Failed to set the active power plan.")