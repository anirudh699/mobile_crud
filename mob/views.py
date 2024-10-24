from django.shortcuts import redirect, render
from django.views import View
from mob.forms import MobileForm
from mob.models import Mobiles



# Create your views here.
class MobileView(View):
    template="mobiles.html"
    form_class=MobileForm
    
    def get(self,request,*args,**kwargs):
        form_instance=self.form_class()

        return render(request,self.template,{"form":form_instance})
    
    def post(self,request,*args,**kwrgs):
        
        form_data=request.POST
        
        form_instance=self.form_class(form_data)
        
        if form_instance.is_valid():
            data=form_instance.cleaned_data
            
            Mobiles.objects.create(
                brand=data.get("brand"),
                model=data.get("model"),
                release_year=data.get("release_year"),
                price=data.get("price")
                
            )
            return redirect("mobile-list")
    

class MobilesList(View):
    template_name="mobile_list.html"
    def get(self,request,*args,**kwargs):
        
        qs=Mobiles.objects.all()
        print(qs)
        return render(request,self.template_name,{"data":qs})
    
    
class MobileDetail(View):
    template_name="mobile_detail.html"
    def get(self,request,*args,**kwrgs):
        id=kwrgs.get("pk")
        qs=Mobiles.objects.get(id=id)
        return render(request,self.template_name,{"data":qs})

        
       
class MobileDeleteview(View):
    template_name="mobile_delete.html"
    def get(self,request,*args,**kwrgs):
        id=kwrgs.get("pk")
        qs=Mobiles.objects.get(id=id).delete()
        return redirect("mobile-list")
    