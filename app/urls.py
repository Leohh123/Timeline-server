from django.urls import path

from . import views

app_name = "app"
urlpatterns = [
    path("stage/now", views.stage_now),
    path("stage/next", views.stage_next),
    path("stage/go", views.stage_go),
    path("stage/jump", views.stage_jump),
    path("task/start", views.task_start),
    path("task/finish", views.task_finish),
    path("task/cancel", views.task_cancel),
    path("task/now", views.task_now),
    path("comment/add", views.comment_add),
    path("plan/list", views.plan_list),
    path("obj/list", views.obj_list),
    path("record", views.record),
    path("test", views.test)
]
