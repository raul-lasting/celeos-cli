
## Initial Setup

Make sure Python 3 is installed:

```bash
$ pip --version
```

If it's not installed, run:

```bash
$ sudo apt install python3
```

All following commands can be run from their respective folders or from the root directory using paths, such as:

```bash
$ python3 IP_address/set_ip_add.py
```

---

## IP Address

### Set IP Address

```bash
$ python3 IP_address/set_ip_add.py
```

- Enter the IP address where CELEOS was installed.
- You can also manually edit the URL file created after running this program.

---

## Login

### User Login

```bash
$ python3 login/login.py
```

- Enter username and password.
- Returns an authentication token.

> ⚠️ You must be logged in to use most of the following scripts.

---

## User 

### Add User

```bash
$ python3 user/add_user.py
```

- Provide requested credentials to create a new user.

### Show Users

```bash
$ python3 user/show_users.py
```

- Displays all registered users and returns a list with them.

### Delete User

```bash
$ python3 user/delete_user.py
```

- Deletes the currently logged-in user.

---

## License

### Activate License

```bash
$ python3 license/license_activation.py
```

- Provide license key and user ID.
- Required files (license key, hardware ID, hardware key) are stored in the `Licence_keys` folder.

### Check License Status

```bash
$ python3 License/license_status.py
```

- Checks if the license is activated.

---

## Scenario 

### Add Profile

1. Add the desired JSON config to `add_profile.json` in the `scenario` folder.
2. Make sure you're logged in.

```bash
$ python3 scenario/add_scenario.py
```

- Adds the profile and returns its name.

### Show Profiles

```bash
$ python3 scenario/show_profiles.py
```

- Lists the names of added profiles and returns the list.

### Update Profile

1. Put the new config in `updated_profile.json`.
2. Make sure the profile already exists.

```bash
$ python3 scenario/update_scenario.py
```

- Updates the profile and returns its name.

### Delete Specific Profiles

```bash
$ python3 scenario/delete_profiles.py
```

- Add profile names separated by space and will return the list of deleted profiles.

### Delete All Profiles

```bash
$ python3 scenario/delete_all_profiles.py
```

- Deletes all profiles for the logged-in user.

---

## Device 

### Load & Start Emulation

1. Add profile name to `load_profile.json`.

```bash
$ python3 device/load_and_start.py
```

- Loads the profile and starts emulation.
- External sync can be configured in `start_emulation()`.

### Start Emulation

```bash
$ python3 device/start.py
```

- Starts emulation using the previously loaded profile.

> To use a different profile, run `load_and_start.py`.

### Stop Emulation

```bash
$ python3 device/stop.py
```

- Stops the running emulation.

### Force Stop (Not Recommended)

```bash
$ python3 device/force_stop.py
```

- Forces emulation to stop.

> 🔒 It is not recommended. Do not use it unless `stop.py` does not work.

### Get Loaded Profile

```bash
$ python3 device/get_loaded_scenario.py
```

- Displays the profile currently loaded on the emulator and returns it.

---

## Status

### Emulator Status

```bash
$ python3 status/emulation_status.py
```

Provides:

- `get_status_log()`: Prints & returns output logs from the emulation.
- `get_status_state()`: Indicates whether emulation is running.
- `get_status_vars()`: Prints & returns emulator variables.

---

### Display emulation logs

```bash
$ python3 status/display_logs.py
```

- Display the emulation logs in real time.

---

## Runtime Parameters

### Add Runtime Parameters

1. Add configurations in `runtime_params.json`.

```bash
$ python3 add_runtime_params.py
```

- Updates parameters while the emulation is running.

### Delete Runtime Parameters

```bash
$ python3 delete_runtime_params.py
```

- Reverts emulation to initial parameters.

---

## SigMF 

### Add Archive

1. Set the path of the sigMF archive in `add_sigmf_archive.py` in `add_sigmf()` function from main.

```bash
$ python3 add_sigmf_archive.py
```

- Adds the sigMF aigMF archive.

### Show SigMF Files

```bash
$ python3 show_sigmf_list.py
```

Includes:

- `show_list()`: Lists all SigMF files and sizes.
- `get_sigmf_archives()`: Lists archive names.
- `get_archives_and_size()`: Lists archive names + sizes.

- They all return the lists.

### Delete SigMF Files

> 🔒 Cannot delete full `.zip` archive—only `.sigmf-data` or `.sigmf-meta`.

1. Set the file name in the API request (`delete_sigmf.py`):

```bash
{url}/sigmf/<sigmf_file>
```

Then run:

```bash
$ python3 delete_sigmf.py
```

---

## Examples

### Combined Scripts for Easy Usage

```bash
$ python3 Examples/add_profile_and_start.py
```

- Adds a profile from `add_profile.json` and starts emulation.

```bash
$ python3 Examples/add_user_and_login.py
```

- Adds a user and logs in automatically.

```bash
$ python3 Examples/create_user_and_start.py
```

- Creates user, logs in, adds profile, and starts emulation.

```bash
$ python3 Examples/login_and_start.py
```

- Logs in, starts emulation using a chosen profile and displays the emulation logs.

```bash
$ python3 Examples/update_and_start.py
```

- Updates a profile from `updated_file.json`, then loads and starts it.

```bash
$ python3 Examples/start_and_display_logs.py
```

- Prints the emulation profiles on the console, then starts the emulation with a chosen profile and displays the logs.

---

## ✅ Tips

- Make sure you're **logged in** before using most scripts.
- Always verify file paths and JSON formats.
- Use the `Examples` folder for common workflows.
