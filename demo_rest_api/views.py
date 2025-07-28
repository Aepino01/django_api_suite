from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import uuid

# Simulación de base de datos local en memoria
data_list = []

# Añadiendo algunos datos de ejemplo para probar el GET
data_list.append({'id': str(uuid.uuid4()), 'name': 'User01', 'email': 'user01@example.com', 'is_active': True})
data_list.append({'id': str(uuid.uuid4()), 'name': 'User02', 'email': 'user02@example.com', 'is_active': True})
data_list.append({'id': str(uuid.uuid4()), 'name': 'User03', 'email': 'user03@example.com', 'is_active': False})  # Item inactivo

class DemoRestApi(APIView):
    name = "Demo REST API"

    def get(self, request):
        # Filtra solo activos
        active_items = [item for item in data_list if item.get('is_active', False)]
        return Response(active_items, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        if 'name' not in data or 'email' not in data:
            return Response({'error': 'Faltan campos requeridos.'}, status=status.HTTP_400_BAD_REQUEST)

        data['id'] = str(uuid.uuid4())
        data['is_active'] = True
        data_list.append(data)
        return Response({'message': 'Dato guardado exitosamente.', 'data': data}, status=status.HTTP_201_CREATED)


class DemoRestApiItem(APIView):
    def get_item(self, id):
        for item in data_list:
            if item["id"] == id:
                return item
        return None

    def put(self, request, id):
        body = request.data
        if "id" not in body:
            return Response({"error": "El campo 'id' es obligatorio en el cuerpo de la solicitud."},
                            status=status.HTTP_400_BAD_REQUEST)
        if body["id"] != id:
            return Response({"error": "El campo 'id' en el cuerpo debe coincidir con el parámetro de la URL."},
                            status=status.HTTP_400_BAD_REQUEST)

        item = self.get_item(id)
        if not item:
            return Response({"error": "Elemento no encontrado."}, status=status.HTTP_404_NOT_FOUND)

        # Reemplazar todos los campos excepto id
        keys_to_keep = ["id"]
        for key in list(item.keys()):
            if key not in keys_to_keep:
                item.pop(key)

        for key, value in body.items():
            if key != "id":
                item[key] = value

        # Asegurar que is_active no se borre accidentalmente
        if "is_active" not in item:
            item["is_active"] = True

        return Response({"message": "Elemento reemplazado exitosamente.", "item": item},
                        status=status.HTTP_200_OK)

    def patch(self, request, id):
        body = request.data
        item = self.get_item(id)
        if not item:
            return Response({"error": "Elemento no encontrado."}, status=status.HTTP_404_NOT_FOUND)

        for key, value in body.items():
            if key == "id" and value != id:
                return Response({"error": "No se puede modificar el campo 'id'."},
                                status=status.HTTP_400_BAD_REQUEST)
            if key != "id":
                item[key] = value

        return Response({"message": "Elemento actualizado parcialmente.", "item": item},
                        status=status.HTTP_200_OK)

    def delete(self, request, id):
        item = self.get_item(id)
        if not item:
            return Response({"error": "Elemento no encontrado."}, status=status.HTTP_404_NOT_FOUND)

        # Eliminación lógica
        item["is_active"] = False

        return Response({"message": "Elemento eliminado lógicamente.", "item": item},
                        status=status.HTTP_200_OK)
