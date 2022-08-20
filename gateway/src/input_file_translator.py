from xml_json_yaml_convert.converter import Converter
MLs = ["pyDict", "xml", "json", "yaml"]
def converter(data = "", input_ml:str = "pyDict", output_ml:str = "pyDict"):
    if input_ml == output_ml:
        return data
    else:
        translator = Converter(data)
        if input_ml == "xml":
            data = translator.from_xml()
        if input_ml == "json":
            data = translator.from_json()
        if input_ml == "yaml":
            data = translator.from_yaml()
        inverce_translator = Converter(data)
        if output_ml == "pyDict":
            return data
        if output_ml == "xml":
            return inverce_translator.to_xml()
        if output_ml == "json":
            return inverce_translator.to_json()
        if output_ml == "yaml":
            return inverce_translator.to_yaml()

