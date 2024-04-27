from rest_framework.response import Response
from rest_framework import status

def response_with_location(self, request):
    """
    Modify the response of the create method to include the location of where
    the new object will be created.
    """
    
    # Since the serializer might be not directly defined in the view, we need to
    # get it from the get_serializer_class method
    serializer_class = self.get_serializer_class() 
    serializer = serializer_class(data=request.data)
    serializer.is_valid(raise_exception=True) #Raise an exception if the serializer is not valid
    serializer.save()
    response = Response(serializer.data, status=status.HTTP_201_CREATED)
    id = str(serializer.data['id'])
    response['Location'] = request.build_absolute_uri() + id
    return response