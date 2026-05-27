from dsa_utils.csthashmap import CustomHashMap

def main():
    user_profiles = CustomHashMap(initial_capacity=8)

    print("--- Inserting Sample Data ---")

    # Standard assignment syntax
    user_profiles["zeta456"] = {"name": "Zeta", "role": "Admin", "active": True}
    user_profiles["bob_the_builder"] = {"name": "Bob", "role": "Developer", "active": True}
    user_profiles["charlie_b"] = {"name": "Charlie", "role": "Tester", "active": False}

    # Test Update user profile
    user_profiles["bob_the_builder"] = {"name": "Bob", "role": "Senior Developer", "active": True}

    # display contents
    print(f"Total profiles stored: {len(user_profiles)}")
    print(f"Current HashMap state:\n{user_profiles}\n")

    print("--- Retrieving Data  ---")

    username = "bob_the_builder"

    if username in user_profiles:
        profile = user_profiles[username]
        assert profile is not None, "Profile should not be None"
        print(f"Successfully retrieved profile for '{username}':")
        # print(profile)
        print(f"    Name: {profile['name']}")
        print(f"    Role: {profile['role']}\n")

    print("--- Deleting Data  ---")

    # target_user = "charlie_b"
    # print(f"Removing user: {target_user}")
    # del user_profiles[target_user]

    inactive_keys = []
    for bucket in user_profiles.buckets:
        for key, value in bucket:
            if value.get("active") is False:
                inactive_keys.append(key)

    for key in inactive_keys:
        print(f"Removing inactive user: {key}")
        del user_profiles[key]

    print(f"Updated total profiles stored: {len(user_profiles)}")
    print(f"Updated HashMap state:\n{user_profiles}\n")


    print("--- Error Handling  ---")

    missing_user = "stranger_dangeriaoetuhoaeutho"
    try:
        print(f"Attempting to fetch missing user '{missing_user}'...")
        _ = user_profiles[missing_user]
    except KeyError as e:
        print(f"Caught expected error: KeyError - The key {e} does not exist.")


if __name__ == '__main__':
    main()
