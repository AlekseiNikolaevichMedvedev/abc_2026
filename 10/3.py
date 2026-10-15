from abc import ABC, abstractmethod
from datetime import datetime
import json
import csv
import io
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom


class DataExporter(ABC):
    @abstractmethod
    def export(self, data) -> None:
        ...

    @abstractmethod
    def get_format_name(self) -> str:
        ...

    def validate_data(self, data) -> bool:
        return bool(data)


class JSONExporter(DataExporter):
    def get_format_name(self) -> str:
        return "JSON"

    def export(self, data) -> None:
        if not self.validate_data(data):
            raise ValueError("Нет данных для экспорта")

        timestamp = datetime.now().isoformat()
        records = [{**record, "export_timestamp": timestamp} for record in data]
        print(json.dumps(records, ensure_ascii=False, indent=2))


class CSVExporter(DataExporter):
    def get_format_name(self) -> str:
        return "CSV"

    def export(self, data) -> None:
        if not self.validate_data(data):
            raise ValueError("Нет данных для экспорта")

        output = io.StringIO()
        writer = csv.DictWriter(output, fieldnames=list(data[0].keys()))
        writer.writeheader()
        writer.writerows(data)
        print(output.getvalue().strip())


class XMLExporter(DataExporter):
    def get_format_name(self) -> str:
        return "XML"

    def export(self, data) -> None:
        if not self.validate_data(data):
            raise ValueError("Нет данных для экспорта")

        root = Element("report")
        for record in data:
            item = SubElement(root, "item")
            for key, value in record.items():
                child = SubElement(item, key)
                child.text = str(value)

        rough = tostring(root, encoding="unicode")
        parsed = minidom.parseString(rough)
        print(parsed.toprettyxml(indent="  ").strip())


if __name__ == "__main__":
    sales_data = [
        {"product": "Laptop", "price": 1000, "quantity": 2},
        {"product": "Mouse", "price": 50, "quantity": 10},
    ]

    for exporter in (JSONExporter(), CSVExporter(), XMLExporter()):
        print(f"Формат: {exporter.get_format_name()}")
        exporter.export(sales_data)
        print()