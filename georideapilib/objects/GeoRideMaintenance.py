import json
import logging

_LOGGER = logging.getLogger(__name__)


class GeoRideMaintenance:

    def __init__(self,
                 name,
                 lastMaintenanceDistance,
                 everyMaintenance,
                 lastMaintenanceDate=None,
                 id=None,
                 todo=None,
                 trackerId=None,
                 dateUnitType=None,
                 createdAt=None,
                 updatedAt=None):
        self.id = id
        self.name = name
        self.todo = todo
        self.trackerId = trackerId
        self.lastMaintenanceDistance = lastMaintenanceDistance
        self.lastMaintenanceDate = lastMaintenanceDate
        self.dateUnitType = dateUnitType
        self.everyMaintenance = everyMaintenance
        self.createdAt = createdAt
        self.updatedAt = updatedAt

    @property
    def get_id(self):
        return self.id

    @property
    def get_name(self):
        return self.name

    @property
    def get_todo(self):
        return self.todo

    @property
    def tracker_id(self):
        return self.trackerId

    @property
    def last_maintenance_distance(self):
        return self.lastMaintenanceDistance

    @property
    def last_maintenance_date(self):
        return self.lastMaintenanceDate

    @property
    def date_unit_type(self):
        return self.dateUnitType

    @property
    def every_maintenance(self):
        return self.everyMaintenance

    @property
    def created_at(self):
        return self.createdAt

    @property
    def updated_at(self):
        return self.updatedAt

    def to_distance_maintenance_json(self):
        return json.dumps({
            "name": self.name,
            "everyMaintenance": self.everyMaintenance,
            "lastMaintenanceDistance": self.lastMaintenanceDistance
        }).encode("utf-8")

    def to_date_maintenance_json(self):
        return json.dumps({
            "name": self.name,
            "everyMaintenance": self.everyMaintenance,
            "lastMaintenanceDate": self.lastMaintenanceDate,
            "dateUnitType": self.dateUnitType
        }).encode("utf-8")

    @staticmethod
    def from_json(json_obj):
        """return new object fromjson"""
        return GeoRideMaintenance(
            name=json_obj['name'],
            id=json_obj['id'],
            todo=json_obj['todo'],
            trackerId=json_obj['trackerId'],
            lastMaintenanceDistance=json_obj['lastMaintenanceDistance'],
            lastMaintenanceDate=json_obj['lastMaintenanceDate'],
            dateUnitType=json_obj['dateUnitType'],
            everyMaintenance=json_obj['everyMaintenance'],
            createdAt=json_obj['createdAt'],
            updatedAt=json_obj['updatedAt']
        )
