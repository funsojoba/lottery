from django.conf import settings

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from lottery.service import SalaryForLifeDraw
from lottery.serializer import TicketSerializer


class LotteryView(viewsets.ViewSet):
    def list(self, request) -> Response:
        return Response(
            {"message": "Hello from LotteryView!"}, status=status.HTTP_200_OK
        )

    @action(methods=["POST"], detail=False)
    def ticket(self, request) -> Response:
        serializer = TicketSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        response = SalaryForLifeDraw.draw(
            plays=[serializer.validated_data["chosen_numbers"]],
            rtp=settings.RTP,
            line_prices=prices,
            jackpot_amount=settings.JACKPOT_AMOUNT,
        )
        return Response({"message": response}, status=status.HTTP_201_CREATED)
