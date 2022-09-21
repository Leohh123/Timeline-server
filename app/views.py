from datetime import datetime, time, timedelta
from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.forms.models import model_to_dict
from django.db.models import F, Q

from .models import Stage, Task, Comment, Plan, Record


def resp(data, msg="ok", code=0):
    return JsonResponse({"code": code, "message": msg, "data": data})


def task_start(request):
    last_task = Task.objects.last()
    if last_task.state == 0:
        return resp(None, "上一个任务尚未完成哦~", 1)
    now_stage = Stage.objects.last()
    task = Task(
        title=request.POST["title"],
        estimated=timedelta(minutes=int(request.POST["estimated"])),
        type=now_stage.type
    )
    task.save()
    return resp(model_to_dict(task))


def _complete_task(new_state):
    task = Task.objects.last()
    if task.state != 0:
        return resp(None, "任务已经完成过了哦~", 1)
    now = datetime.now()
    task.actual = now - task.head
    task.tail = now
    task.state = new_state
    task.save()
    return task


def task_finish(request):
    task = _complete_task(1)
    return resp(model_to_dict(task))


def task_cancel(request):
    lastTask = Task.objects.last()
    now = datetime.now()
    if lastTask.state == 0 and now - lastTask.head < timedelta(minutes=1):
        lastTask.delete()
        return resp(None, u"已成功撤销任务")
    task = _complete_task(2)
    return resp(None, u"已成功取消任务")


def task_now(request):
    task = Task.objects.last()
    if task.state == 0:
        return resp(model_to_dict(task))
    return resp(None)


def plan_list(request):
    now = datetime.now()
    enabled_plans = Plan.objects.filter(
        Q(day=now.weekday()) | Q(day=7)).order_by("clock")
    disabled_plans = Plan.objects.filter(
        ~Q(day=now.weekday()) & ~Q(day=7)).order_by("day", "clock")
    enabled_dicts = list(map(model_to_dict, enabled_plans))
    disabled_dicts = list(map(model_to_dict, disabled_plans))
    return resp({"enabled": enabled_dicts, "disabled": disabled_dicts})


def stage_now(request):
    stage = Stage.objects.last()
    return resp(model_to_dict(stage))


def _next_stage(now_datetime):
    result = Plan.objects.filter(
        Q(day=now_datetime.weekday()) | Q(day=7),
        clock__gt=now_datetime.time()
    ).order_by("clock", "day")
    if result.exists():
        plan = result.first()
        now_estimated = now_datetime.replace(
            hour=plan.clock.hour,
            minute=plan.clock.minute,
            second=plan.clock.second,
            microsecond=plan.clock.microsecond
        )
        stage = Stage(title=plan.title,
                      estimated=now_estimated, type=plan.type)
    else:
        now = datetime.now()
        plan = Plan.objects.filter(
            Q(day=now.weekday()) | Q(day=7)
        ).order_by("clock", "day").first()
        estimated = now.replace(
            hour=plan.clock.hour,
            minute=plan.clock.minute,
            second=plan.clock.second,
            microsecond=plan.clock.microsecond
        )
        stage = Stage(title=plan.title, estimated=estimated, type=plan.type)
    return stage


def stage_next(request):
    now_stage = Stage.objects.last()
    next_stage = _next_stage(now_stage.estimated)
    return resp(model_to_dict(next_stage))


def stage_go(request):
    task = Task.objects.last()
    if task.state == 0:
        return resp(None, u"还有尚未完成的任务哦~", 1)
    now_stage = Stage.objects.last()
    next_stage = _next_stage(now_stage.estimated)
    next_stage.save()
    return resp(model_to_dict(next_stage))


def stage_jump(request):
    plan = Plan.objects.get(id=int(request.POST["pid"]))
    now = datetime.now()
    estimated = now.replace(
        hour=plan.clock.hour,
        minute=plan.clock.minute,
        second=plan.clock.second,
        microsecond=plan.clock.microsecond
    )
    jump_stage = Stage(title=plan.title, estimated=estimated, type=plan.type)
    jump_stage.save()
    return resp(model_to_dict(jump_stage))


def comment_add(request):
    token = request.COOKIES.get("token")
    name = request.POST.get("name", "").strip()
    if token == "123456":
        name = "Leohh"
    elif name == "":
        return resp(None, u"还不知道你叫什么呢~", 1)
    elif name == "Leohh":
        return resp(None, u"不许用主人的名字！", 1)
    comment = Comment(name=name, content=request.POST["content"])
    comment.save()
    return resp(model_to_dict(comment))


def obj_list(request):
    start_time = datetime.fromtimestamp(int(request.GET["from"]))
    end_time = datetime.fromtimestamp(int(request.GET["to"]))
    objs = []
    objs.extend(Stage.objects.filter(
        actual__range=(start_time, end_time)
    ))
    objs.extend(Task.objects.filter(
        head__range=(start_time, end_time)
    ))
    objs.extend(Comment.objects.filter(
        moment__range=(start_time, end_time)
    ))
    objs.sort(key=lambda o: o.key())
    obj_dicts = list(map(lambda m: {
        "component": m.__class__.__name__.lower(),
        **model_to_dict(m)
    }, objs))
    return resp(obj_dicts)


def record(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    token = request.COOKIES.get("token") or ""
    record = Record(ip=ip, token=token)
    record.save()
    return resp(model_to_dict(record))


def test(request):
    # now = datetime.fromtimestamp(1662600835)
    # plan = _match_plan(time(13, 19, 0), 2)
    # return resp(model_to_dict(plan))
    pass
