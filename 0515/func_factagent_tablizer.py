# 0515/func_tablizers.py
import inst_factagent
from dataclasses import is_dataclass

def flatten_list(nested, seen=None):
    if seen is None:
        seen = set()
    if id(nested) in seen:
        return  # Prevent infinite recursion
    seen.add(id(nested))
    for item in nested:
        if isinstance(item, list):
            yield from flatten_list(item, seen)
        else:
            yield item

def flatten_attributes(obj):
    """
     Recursively expand the attributes of an object into a list of (attribute name, value) pairs.
    """
    result = []
    for attr, value in vars(obj).items():
        # If list
        if isinstance(value, list): #  If the contents of the list are primitive types, combine them into a comma-separated string.
            #  Recursively flatten the list
            flat = list(flatten_list(value))
            #  If all elements are primitive types, join them with commas
            if all(isinstance(item, (str, int, float, bool, type(None))) for item in flat):
                joined = ', '.join(map(str, flat))
                result.append((attr, joined))
            else:
                #  If the object is a dataclass or has a dict, process it recursively
                for item in flat:
                    if hasattr(item, "__dict__") or is_dataclass(item):
                        result.extend(flatten_attributes(item))
                    else:
                        result.append((attr, item))
        #  If the object is a dataclass or has a dict, process it recursively
        elif hasattr(value, "__dict__") or is_dataclass(value):
            result.extend(flatten_attributes(value))
        else:
            result.append((attr, value))
    return result

def tablize_attr_and_iv(all_instances):
    tables = []
    # If inst_atomagent.AtomAgent.ALL_ATOMAGENT does not exist, iterate directly over the list
    # e.g. for atomagent in [inst_atomagent]:
    for i in all_instances:
        table = f"<table id='{i.name}'>\n"
        for attr, value in flatten_attributes(i):
            table += f"<tr><th>{attr}</th><td>{value}</td></tr>\n"
        table += "</table>"
        tables.append(table)
    tables_str = ''.join(tables)
    # CSSを追加
    css = """
    <style>

    
    </style>
    """
    return css + tables_str


html_content = tablize_attr_and_iv(inst_factagent.FactAgent.ALL_FACTAGENT)
with open('output_func_factagent_tablizer.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
