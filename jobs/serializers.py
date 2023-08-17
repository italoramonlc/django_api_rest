from rest_framework.reverse import reverse
from rest_framework import serializers
from .models import Job

class JobSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Job
        exclude = ("is_active",)
        extra_kwargs = {
            "title":{"min_length":10},
            "salary": {"min_value": 1000},
            "description": {"min_length": 10,"max_length":500},
            "company": {"min_length": 3},
            "location": {"min_length": 10},
        }

    def get_links(self,obj):
        links = []
        self_link = reverse("jobs:detail",request=self.context["request"],kwargs={"pk":obj.pk})
        links.append(
            {
                "type":"GET",
                "rel":"self",
                "href":self_link,
            }
        )
        links.append(
            {
                "type":"PUT",
                "rel":"update_job",
                "href":self_link,
            }
        )
        links.append(
            {
                "type":"DELETE",
                "rel":"delete_job",
                "href":self_link,
            }
        )
        return links


    # def validate_title(self,value):
    #     if len(value) < 10:
    #         raise serializers.ValidationError("Deve ter pelo menos 10 caracteres")
    #     return value
    #
    # def validate_salary(self,value):
    #     if value < 50:
    #         raise serializers.ValidationError("Deve ser maior que 50")
    #     return value
    #
    # def validate_description(self,value):
    #     if len(value) < 10:
    #         raise serializers.ValidationError("Deve ter pelo menos 10 caracteres")
    #     return value
    #
    # def validate_company(self,value):
    #     if len(value) < 3:
    #         raise serializers.ValidationError("Deve ter pelo menos 3 caracteres")
    #     return value
