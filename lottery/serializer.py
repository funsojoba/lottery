from rest_framework import serializers


class TicketSerializer(serializers.Serializer):
    number_of_lines = serializers.IntegerField()
    chosen_numbers = serializers.ListField(
        child=serializers.IntegerField(), min_length=5, max_length=5
    )
