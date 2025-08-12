# landing_api/views.py  (ojo: el nombre de archivo suele ser views.py)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from firebase_admin import db
from datetime import datetime

class LandingAPI(APIView):
    collection_name = "landing_entries"

    def get(self, request):
        try:
            ref = db.reference(self.collection_name)
            data = ref.get()
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            data = dict(request.data)  # copia mutables

            now = datetime.now()
            data["timestamp"] = now.strftime("%d/%m/%Y, %I:%M:%S %p").lower() \
                .replace('am','a. m.').replace('pm','p. m.')

            ref = db.reference(self.collection_name)
            new_ref = ref.push(data)   # <-- si falla, se va al except
            data["id"] = new_ref.key

            # Lee de nuevo para confirmar persistencia (opcional):
            saved = db.reference(f"{self.collection_name}/{new_ref.key}").get()

            return Response({
                "message": "Dato guardado exitosamente.",
                "data": saved or data
            }, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({
                "message": "Error guardando en Realtime Database.",
                "error": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
