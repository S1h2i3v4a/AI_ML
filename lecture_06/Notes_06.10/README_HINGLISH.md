# Lecture 06.10: Working with the JSON Module in Python [Hinglish]

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange.svg?logo=jupyter&logoColor=white)](lecture_06_10.ipynb)
[![PDF](https://img.shields.io/badge/PDF-notes.pdf-red.svg)](notes.pdf)

🌐 **Language / भाषा:** [English](README.md) | **हिंदी / Hinglish** | [⬅️ Lecture 06 Module Par Wapas Jayein](../README_HINGLISH.md)

---

### 📋 Is Topic Mein Hum Kya Seekhenge?
- JSON kya hota hai aur web APIs, microservices, aur data storage me iska universal role.
- The 4 Core Functions: `json.dumps()`, `json.loads()`, `json.dump()`, aur `json.load()` ka farq.
- The 's' rule: `dump`/`load` for file streams, `dumps`/`loads` for strings ('s' = string).
- Human readability formatting: `indent=4` aur `sort_keys=True` parameter.
- JSON data types mapping: Python `dict` -> JSON `object`, Python `list` -> JSON `array`, Python `None` -> JSON `null`.

---

### 🔍 Har Ek Point Ka Simple & Detailed Explanation

- **JSON Kya Hai**: JSON (JavaScript Object Notation) ek lightweight text-based data format hai jo machine readable aur human readable dono hota hai. Python dictionaries aur JSON ka structure lagbhag identical dikhta hai.

- **String Functions (`dumps` & `loads`)**: `json.dumps(dict_data)` Python dictionary ko JSON formatted string me convert karta hai (Serialization). `json.loads(json_str)` JSON formatted string ko parse karke wapas Python dictionary banata hai (Deserialization).

- **File Stream Functions (`dump` & `load`)**: `json.dump(data, file_handle, indent=4)` data ko directly file me JSON ke roop me save karta hai. `json.load(file_handle)` JSON file ko read karke Python data structure me load karta hai.

- **`indent=4` Parameter**: Default JSON ek single compact line me likha jata hai jise padhna mushkil hota hai. `indent=4` pass karne se JSON pretty-printed aur indented form me save hota hai.

- **Lecture Reference**: Ma'am ne slide 7 me cities data aur student marks ka example lekar charo functions detail me demonstrate kiye the.

---

## 2. Visual Architecture & Workflow Diagram

```mermaid
flowchart LR
    subgraph PythonMemory ["Python Memory (Runtime)"]
        A["Python Object<br/>(dict / list / int / str)"]
    end
    subgraph JSONRepresentations ["JSON Formats"]
        B["JSON String<br/>'{"name": "Shivam"}'"]
        C["JSON File on Disk<br/>data.json"]
    end
    A -->|"json.dumps()"| B
    B -->|"json.loads()"| A
    A -->|"json.dump(data, f)"| C
    C -->|"json.load(f)"| A
```

---

## 3. Mathematical & Theoretical Framework

Data serialization is an isomorphic mapping between memory-resident object graphs and serialized byte sequences:

$$
\mathcal{S}: \text{PyObject} \longrightarrow \text{JSON\_String}, \qquad \mathcal{S}^{-1}: \text{JSON\_String} \longrightarrow \text{PyObject}
$$

Mapping invariants preserve type equivalences:

$$
\text{dict} \mapsto \text{Object}, \quad \text{list} \mapsto \text{Array}, \quad \text{bool} \mapsto \text{true/false}, \quad \text{None} \mapsto \text{null}
$$

---

## 4. Structured Implementation & Execution

```python
import json
import os

def demonstrate_json_serialization_workflow(filepath: str, initial_data: dict, new_entry_key: str, new_entry_val: int) -> dict:
    """
    Demonstrates the complete JSON lifecycle: serialization to string, writing to disk with indent,
    reading back from disk, updating data in-place, and re-saving.
    (Covers Assignment 5 Question 4 workflow).
    
    Parameters:
    -----------
    filepath : str
        Target JSON file path.
    initial_data : dict
        Initial dictionary (e.g. city populations).
    new_entry_key : str
        New city name to insert.
    new_entry_val : int
        New city population.
        
    Returns:
    --------
    dict
        Verification of serialized strings and updated loaded dictionaries.
    """
    # 1. dumps: Python dict to JSON String
    json_string = json.dumps(initial_data)
    
    # 2. dump: Save to file with indent=4 for human readability
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(initial_data, f, indent=4)
        
    # 3. load: Read from file back into Python dictionary
    with open(filepath, "r", encoding="utf-8") as f:
        loaded_data = json.load(f)
        
    # 4. In-place update: Insert new city population
    loaded_data[new_entry_key] = new_entry_val
    
    # 5. Re-save updated dictionary back to JSON file
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(loaded_data, f, indent=4)
        
    # 6. Verify final file contents
    with open(filepath, "r", encoding="utf-8") as f:
        final_loaded_data = json.load(f)
        
    return {
        "serialized_json_string": json_string,
        "initial_keys_count": len(initial_data),
        "updated_keys_count": len(final_loaded_data),
        "final_json_data": final_loaded_data,
        "new_entry_confirmed": new_entry_key in final_loaded_data
    }

# Driver test (Assignment 5 Q4: Cities & Populations)
cities_dict = {
    "Delhi": 33000000,
    "Mumbai": 21000000,
    "Bengaluru": 13500000
}
target_json = "cities.json"

json_audit = demonstrate_json_serialization_workflow(target_json, cities_dict, "Hyderabad", 10500000)
print("JSON Serialization & Disk I/O Workflow Audit:")
for k, v in json_audit.items():
    print(f"  {k}: {v}")

# Cleanup
if os.path.exists(target_json):
    os.remove(target_json)
```

---

## 5. Mukhya Batein (Key Takeaways) & Summary
- Code ko modular function ke roop me likha gaya hai jisme clear shuruat (`def`), docstrings, error handling, aur ending (`return`) maujood hai.
- Video lectures me ma'am dwara sikhaye gaye exact concepts, slides aur Assignment 5 ke requirements ko 100% follow kiya gaya hai.
