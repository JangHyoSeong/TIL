from django import forms
from .models import travels

class TravelsForm(forms.ModelForm):
    location = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': '제주도',
            }
        )
    )

    start_date = forms.DateField(
        input_formats=['%Y-%m-%d'],  # 입력 형식을 여기에 지정합니다
        widget=forms.DateInput(
            attrs={
                'placeholder': '2022-02-22',
            }
        )
    )

    end_date = forms.DateField(
        input_formats=['%Y-%m-%d'],  # 입력 형식을 여기에 지정합니다
        widget=forms.DateInput(
            attrs={
                'placeholder': '2022-02-22',
            }
        )
    )

    class Meta:
        model = travels
        fields = '__all__'
