import json
import logging

_LOGGER = logging.getLogger(__name__)


class GeorideMaintenance:

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

    @staticmethod
    def from_json(json):
        """return new object fromjson"""
        return GeorideMaintenance(
            name=json['name'],
            id=json['id'],
            todo=json['todo'],
            trackerId=json['trackerId'],
            lastMaintenanceDistance=json['lastMaintenanceDistance'],
            lastMaintenanceDate=json['lastMaintenanceDate'],
            dateUnitType=json['dateUnitType'],
            everyMaintenance=json['everyMaintenance'],
            createdAt=json['createdAt'],
            updatedAt=json['updatedAt']
        )
