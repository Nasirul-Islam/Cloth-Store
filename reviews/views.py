# from django.shortcuts import render, redirect
# from .forms import ReviewForm

# def submit_review(request, item_id):
#     if request.method == 'POST':
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             review = form.save(commit=False)
#             review.user = request.user 
#             review.item_id = item_id
#             review.save()
#             return redirect('store', item_id=item_id)  
#     else:
#         form = ReviewForm()
#     return render(request, 'review_form.html', {'form': form})
