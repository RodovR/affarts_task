from django.db import models
from human.models import HumanModel


class HumanActionsModel(models.Model):
    human = models.ForeignKey(HumanModel, on_delete=models.CASCADE)
    action_description = models.TextField(max_length=200)
    action_rate = models.IntegerField()
    action_date = models.DateField(auto_now=False, auto_now_add=False)

    @staticmethod
    def get_human_info(first_name=str):
        count = 0
        inf_dict = {}
        scores_dict = {'act_scores': []}
        positive = []
        neutral = []
        negative = []
        human = HumanModel.objects.filter(first_name=first_name)[0]
        all_action = HumanActionsModel.objects.all()
        for i in all_action:
            if i.human_id == human.pk:
                count += 1
                if i.action_rate < 5:
                    scores_dict['act_scores'].append(i.action_rate)
                    negative.append(i.action_rate)
                elif i.action_rate == 5:
                    scores_dict['act_scores'].append(i.action_rate)
                    neutral.append(i.action_rate)
                else:
                    scores_dict['act_scores'].append(i.action_rate)
                    positive.append(i.action_rate)
        avg_rate = sum(scores_dict['act_scores']) / count
        inf_dict['Имя'] = human.first_name
        inf_dict['Фамилия'] = human.second_name
        inf_dict['Средняя оценка его поступков за все время'] = avg_rate
        inf_dict['Количество положительных поступков'] = len(positive)
        inf_dict['Количество нейтральных поступков'] = len(neutral)
        inf_dict['Количество отрицательных поступков'] = len(negative)
        return inf_dict

# ==============ЗАПРОС===================

# --Написать запрос, который позволит вывести:
# --Количество зарегистрированных в браке людей, чье состояние о работе неизвестно, проживающих в городе N и имеющих средний рейтинг всех поступков выше 6.*/
#
# SELECT COUNT(*) FROM human_humanmodel AS HHM
# INNER JOIN residences_place_residencesplace AS RPR
# ON  HHM.id == RPR.registered_name_id
# INNER JOIN human_actions_humanactionsmodel AS HAHM
# ON HAHM.human_id == HHM.id
# WHERE HHM.is_marriage == 1 AND HHM.is_unemployed == True AND HAHM.action_rate > 6;

# Немножечко накосячил с условием, что переменная HHM.is_unemployed может иметь статус НЕИЗВЕСТНО, тк писал на скорую руку.
# Поэтому, за значение по умолчанию использовал TRUE.

# =======================================
