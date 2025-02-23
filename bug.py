def function_with_uncommon_error(x):
    try:
        result = 10 / x
    except ZeroDivisionError:
        return "Division by zero"
    except TypeError:
        return "Unsupported type"
    except Exception as e:
        return f"An unexpected error occurred: {e}"
    return result

print(function_with_uncommon_error(0))
print(function_with_uncommon_error('a'))
print(function_with_uncommon_error(2))