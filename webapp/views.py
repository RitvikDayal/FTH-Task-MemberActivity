from .models import Member
from .serializers import MemberSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def home(request):
    api_urls = {
        'List': '/activity-logs/',
        'Member Activity Log': '/member-activity/<int:pk>/',
        'Delete Activity Log': '/log-delete/<int:pk>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def activityLogs(request):
    try:
        members = Member.objects.all()
        serializer = MemberSerializer(data=members, many=True)
        serializer.is_valid()
        return Response({"ok":True,"members": serializer.data})
    
    except Exception as e:
        print("Exception",e)

        return Response({"ok":False,"message": str(e)})


@api_view(['GET'])
def memberActivityLog(request, pk):
    try:
        members = Member.objects.get(id=pk)
        serializer = MemberSerializer(data=members)
        serializer.is_valid()
        return Response({"ok":True,"members": serializer.data})
    
    except Exception as e:
        print("Exception",e)

        return Response({"ok":False,"message": str(e)})


@api_view(['DELETE'])
def memberLogDelete(request, pk):
    member = Member.objects.get(id=pk)
    member.delete()

    return Response('Item Successfully Deleted')