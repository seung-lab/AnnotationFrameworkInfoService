import annotationinfoservice.datasets.models as models
from flask_marshmallow import Marshmallow
import marshmallow
ma = Marshmallow()

class AlignedVolumeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = models.AlignedVolume

class DataStackSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = models.DataStack
        
    aligned_volume = ma.HyperlinkRelated("api.Annotation Infoservice_aligned_volume_id_resource", "id")

class DataStackSchemaFull(marshmallow.Schema):
    aligned_volume = marshmallow.fields.Nested(AlignedVolumeSchema)
    segmentation_source = marshmallow.fields.String()
    analysis_database = marshmallow.fields.String()
    viewer_site = marshmallow.fields.String()
    synapse_table= marshmallow.fields.String()
    soma_table = marshmallow.fields.String()
    local_server = marshmallow.fields.String()
    description = marshmallow.fields.String()

class PermissionGroupSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = models.PermissionGroup

class TableMappingSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = models.TableMapping
    permissiongroup = ma.HyperlinkRelated("api.Annotation Infoservice_permission_group_id_resource", "id")

class TableMappingFullSchema(marshmallow.Schema):
    permission_group = marshmallow.fields.Nested(PermissionGroupSchema)
    table_name = marshmallow.fields.String()
    service_name = marshmallow.fields.String()
    