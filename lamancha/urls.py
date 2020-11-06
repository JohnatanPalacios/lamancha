# Django
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


from lamancha import views as local_views
from users import views as users_views
from books import views as books_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', local_views.home, name='home'),

    # vistas de usuario
    path('users/signup/', users_views.signup_view, name='signup'),
    path('users/login/', users_views.login_view, name='login'),
    path('users/logout/', users_views.logout_view, name='logout'),
    path('users/profile/main/', users_views.profile_main, name='profile_main'),
    path('users/profile/payment_methods/', users_views.profile_payment_methods, name='profile_payment_methods'),


    # vistas de libros
    path('books/details/<pk>', books_views.BookDetailView.as_view(), name='book_details'),
    path('search/results/', books_views.search, name='search'),

    # reset password group
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='users/reset_password.html', html_email_template_name='users/send_email.html',), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


'''
1- submit email form                                PasswordResetView.as_view()
2- email sent success massage                       PasswordResetDoneView.as_view()
3- link to password reset from in email             PasswordConfirmView.as_view()
4- password successfully changed messsage           PasswordResetCompleteView.as_view()
'''
