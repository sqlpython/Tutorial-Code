


def who_is_online(friends):
    
friends = [
    {"username": "Alice", "status": "online", "lastActivity": 10},
    {"username": "Lucy", "status": "offline", "lastActivity": 22},
    {"username": "Bob", "status": "online", "lastActivity": 104}
    
    """
    Categorize friends into online, offline, and away status.
    
    Args:
        friends: List of dictionaries with 'username', 'status', and 'lastActivity'
        
    Returns:
        Dictionary with 'online', 'offline', and/or 'away' keys containing usernames
    """
    # chk if input is empty
    if not friends:
        return {}
    
    result = {}
    
    for friend in friends:
        username = friend['username']
        status = friend['status']
        last_activity = friend['lastActivity']
        
        # Determine category
        if status == 'offline':
            category = 'offline'
        elif status == 'online' and last_activity > 10:
            category = 'away'
        else:  # online and lastActivity <= 10
            category = 'online'
        
        # Add to result
        if category not in result:
            result[category] = []
        result[category].append(username)
    
    return result


print(who_is_online(friends)
# Output: {'online': ['Alice'], 'offline': ['Lucy'], 'away': ['Bob']}

