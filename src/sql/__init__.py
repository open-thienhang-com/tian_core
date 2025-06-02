import datetime


def map_fields_values(field_names, values):
  """Maps field names to values from two arrays, with customization options.

  Args:
      field_names: A list of field names.
      values: A list of values (can have a different length than field_names).

  Returns:
      A dictionary mapping field names to their corresponding values.

  Raises:
      ValueError: If there are more values than field names (optional).
  """

  field_value_map = {}
  for i, name in enumerate(field_names):
    if i < len(values):
      formated_data = values[i]
      if isinstance(values[i] , datetime.datetime):
                formated_data = str(values[i])
      field_value_map[name] = formated_data
    else:
      # Handle missing values (e.g., set to None, raise an error)
      field_value_map[name] = None  # Example: Set to None

  # Optional check for extra values (can be removed if not needed)
  if len(values) > len(field_names):
    raise ValueError("More values provided than field names")

  return field_value_map

def find_index_by_property(data, property_name, value):
  """Finds the index of an object in a list based on a property value.

  Args:
    data: The list of objects.
    property_name: The name of the property to check.
    value: The value to search for.

  Returns:
    The index of the object if found, -1 otherwise.
  """
  for index, item in enumerate(data):
    if item[property_name] == value:
      return index
  return -1
