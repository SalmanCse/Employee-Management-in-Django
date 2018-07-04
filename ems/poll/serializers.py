from rest_framework import serializers

from poll.models import Question

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = [
            "id",
            "title",
            "status",
            "created_by"

        ]

        # def create(self, validated_data): //serializers.py no need delete korte paro,it is use for restframework
        #   pass
