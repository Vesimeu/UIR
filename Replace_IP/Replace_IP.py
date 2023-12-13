import psutil
import wmi
import ctypes
import logging
import sys


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


logging.basicConfig(filename='network_config.log', level=logging.DEBUG)
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)


def get_network_adapters():
    try:
        psutil_adapters = list(psutil.net_if_stats().keys())
        wmi_adapters = {adapter.Description: adapter for adapter in wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=True)}
        adapters = list(set(psutil_adapters).union(wmi_adapters.keys()))
        return adapters, wmi_adapters
    except Exception as e:
        logging.error(f"Ошибка при получении сетевых адаптеров: {e}")
        return None, None


def try_change_settings(adapter_name, ip, subnetmask, gateway):
    try:
        nic_configs = wmi.WMI().Win32_NetworkAdapterConfiguration(Caption=adapter_name)
        new_config = wmi.WMI().Win32_NetworkAdapterConfiguration(Caption = "MediaTek Wi-Fi 6 MT7921 Wireless LAN Card")
        print(nic_configs, " - it's nic")
        print(new_config, " - it's new config")
        if nic_configs:
            nic = nic_configs[0]
            # Получаем текущие настройки
            current_ip = nic.IPAddress[0] if nic.IPAddress else None
            current_subnetmask = nic.IPSubnet[0] if nic.IPSubnet else None
            current_gateway = nic.DefaultIPGateway[0] if nic.DefaultIPGateway else None

            # Проверяем, нужно ли вообще менять настройки
            if current_ip == ip and current_subnetmask == subnetmask and current_gateway == gateway:
                logging.info(f"Настройки для адаптера {adapter_name} уже соответствуют введенным значениям.")
                print(f"Настройки для адаптера {adapter_name} уже соответствуют введенным значениям.")
                return True

            # Устанавливаем новые настройки
            nic.EnableStatic(IPAddress=[ip], SubnetMask=[subnetmask])
            nic.SetGateways(DefaultIPGateway=[gateway])

            logging.info(f"Настройки успешно изменены для адаптера: {adapter_name}")
            print(f"Настройки успешно изменены для адаптера: {adapter_name}")
            return True
        else:
            logging.error(f"Адаптер {adapter_name} не найден.")
            print(f"Адаптер {adapter_name} не найден.")
            return False
    except Exception as e:
        logging.error(f"Произошла ошибка при изменении настроек для адаптера {adapter_name}: {e}")
        print(f"Произошла ошибка при изменении настроек для адаптера {adapter_name}. Подробности в логах.")
        return False


def main():
    if is_admin():
        print("зашёл сюда")
        nic_descriptions, nic_dict = get_network_adapters()

        if nic_descriptions and nic_dict:
            print("Доступные сетевые адаптеры:")
            for i, description in enumerate(nic_descriptions, start=1):
                print(f"{i}. {description}")

            selected_description = input("Введите часть описания сетевого адаптера: ")
            matching_adapters = [description for description in nic_descriptions if description.startswith(selected_description)]

            if matching_adapters:
                print("Найденные адаптеры:")
                for i, description in enumerate(matching_adapters, start=1):
                    print(f"{i}. {description}")

                try:
                    index = int(input("Выберите номер сетевого адаптера: ")) - 1
                    selected_adapter_description = matching_adapters[index]

                    ip = input("Введите новый IP-адрес: ")
                    subnetmask = input("Введите новую маску подсети: ")
                    gateway = input("Введите новый шлюз: ")

                    selected_adapter = nic_dict.get(selected_adapter_description)


                    if selected_adapter:
                        # print(selected_adapter.Description, " " , selected_adapter)
                        success = try_change_settings(selected_adapter.Description, ip, subnetmask, gateway)

                        if not success:
                            print(f"Не удалось изменить настройки. Проверьте логи для получения дополнительной информации.")
                    else:
                        print(f"Адаптер с описанием '{selected_adapter_description}' не найден.")
                        logging.error(f"Адаптер с описанием '{selected_adapter_description}' не найден.")
                except (ValueError, IndexError):
                    logging.error("Ошибка при выборе сетевого адаптера")
            else:
                print(f"Адаптер с описанием, начинающимся с '{selected_description}', не найден.")
                logging.error(f"Адаптер с описанием, начинающимся с '{selected_description}', не найден.")
        else:
            print("Не удалось получить информацию о сетевых адаптерах. "
                  "Проверьте логи для получения дополнительной информации.")
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)


if __name__ == "__main__":
    main()
