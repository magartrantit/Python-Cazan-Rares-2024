def validate_dict(rules, d):
    for key, prefix, middle, suffix in rules:
        if key not in d:
            return False
        
        value = d[key]
        
        if not value.startswith(prefix):
            return False
        
        if not value.endswith(suffix):
            return False
        
        if middle not in value[len(prefix):-len(suffix) or None]:
            return False
    
    return True

rules = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
d = {"key1": "come inside, it's too cold out", "key2": "start something in the middle of winter"}
result = validate_dict(rules, d)
print(result)