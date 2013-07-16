from django import forms
from django.forms.formsets import formset_factory
from django.shortcuts import render_to_response
from django.template import RequestContext


class ArticleForm(forms.Form):
    title = forms.CharField()
    pub_date = forms.DateField()


def manage_articles(request):
    ArticleFormSet = formset_factory(ArticleForm)
    if request.method == 'POST':
        article_formset = ArticleFormSet(request.POST,
                                         request.FILES,)
        if article_formset.is_valid():
            # do something with the cleaned_data on the formsets.
            pass
    else:
        article_formset = ArticleFormSet()
    return render_to_response('manage_articles.html', {
        'formset': article_formset,
    }, context_instance=RequestContext(request))
