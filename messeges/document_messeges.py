from modules.message import Message



class GetFile1(Message):
    def request(self):
        return "1"

    def response(self):
        self.server.upload_document(self.event,
                                    "documents/1_Zayavlenie_o_prodlenii_sroka_promejutochnoyi_attestacii.docx",
                                    "Заявление о продлении срока промежуточной аттестации")
        return "Готово!"


class GetFile2(Message):
    def request(self):
        return "2"

    def response(self):
        self.server.upload_document(self.event, "documents/2_Zayavlenie_o_perezachtenii_disciplin.docx",
                                    "Заявление о перезачтении дисциплин")
        return "Готово!"


class GetFile3(Message):
    def request(self):
        return "3"

    def response(self):
        self.server.upload_document(self.event,
                                    "documents/3_Zayavlenie_ob_perevode_iz_drugogo_vuza_v_PNIPU_dlya_prodoljeniya_obucheniya_po_programme_aspiranturi_(2).docx",
                                    "Заявление об переводе из другого вуза в ПНИПУ для продолжения обучения по программе аспирантуры")
        return "Готово!"


class GetFile4(Message):
    def request(self):
        return "4"

    def response(self):
        self.server.upload_document(self.event, "documents/4_Zayavlenie_o_perehode_s_programmi_na_programmu_PNIPU.doc",
                                    "Заявление о переходе с программы на программу ПНИПУ")
        return "Готово!"


class GetFile5(Message):
    def request(self):
        return "5"

    def response(self):
        self.server.upload_document(self.event,
                                    "documents/5_Zayavlenie_o_perevode_na_uskorennoe_obuchenie_za_schet_povisheniya_intensivnosti_osvoeniya_programmi.doc",
                                    "Заявление о переводе на ускоренное обучение за счет повышения интенсивности освоения программы")
        return "Готово!"


class GetFile6(Message):
    def request(self):
        return "6"

    def response(self):
        self.server.upload_document(self.event,
                                    "documents/6_Zayavlenie_o_perevode_na_uskorennoe_obuchenie_za_schet_perezacheta_ranee_sdannih_disciplin.doc",
                                    "Заявление о переводе на ускоренное обучение за счет перезачета ранее сданных дисциплин")
        return "Готово!"


class GetFile7(Message):
    def request(self):
        return "7"

    def response(self):
        self.server.upload_document(self.event,
                                    "documents/7_Zayavlenie_ob_otchislenii_iz_PNIPU_v_svyazi_s_perevodom_dlya_prodoljeniya_obucheniya_v_dr.vuze.doc",
                                    "Заявление об отчислении из ПНИПУ в связи с переводом для продолжения обучения в др.вузе")
        return "Готово!"


class GetFile8(Message):
    def request(self):
        return "8"

    def response(self):
        self.server.upload_document(self.event,
                                    "documents/8_Zayavlenie_ob_otchislenii_iz_PNIPU_po_sobstvennomu_jelaniyu.doc",
                                    "Заявление об отчислении из ПНИПУ по собственному желанию")
        return "Готово!"


class GetFile9(Message):
    def request(self):
        return "9"

    def response(self):
        self.server.upload_document(self.event, "documents/9_Zayavlenie_o_vosstanovlenii_v_PNIPU.doc",
                                    "Заявление о восстановлении в ПНИПУ")
        return "Готово!"


class GetFile10(Message):
    def request(self):
        return "10"

    def response(self):
        self.server.upload_document(self.event,
                                    "documents/10_Zayavlenie_ob_apellyacii_ocenki_na_vstupitelnih_ekzamenah.doc",
                                    "Заявление об апелляции оценки на вступительных экзаменах")
        return "Готово!"


class GetFile11(Message):
    def request(self):
        return "11"

    def response(self):
        self.server.upload_document(self.event,
                                    "documents/11_Zayavlenie_o_smene_familii.doc",
                                    "Заявление о смене фамилии")
        return "Готово!"


class GetFile12(Message):
    def request(self):
        return "12"

    def response(self):
        self.server.upload_document(self.event, "documents/12_Zayavlenie_o_smene_nauchnogo_rukovoditelya.doc",
                                    "Заявление о смене научного руководителя")
        return "Готово!"


class GetFile13(Message):
    def request(self):
        return "13"

    def response(self):
        self.server.upload_document(self.event,
                                    "documents/13_Zayavlenie_o_predostavlenii_akademicheskogo_otpuska.doc",
                                    "Заявление о предоставлении академического отпуска")
        return "Готово!"


class GetFile14(Message):
    def request(self):
        return "14"

    def response(self):
        self.server.upload_document(self.event,
                                    "documents/14_Zayavlenie_o_predostavlenii_otpuska_po_beremennosti_i_rodam.doc",
                                    "Заявление о предоставлении отпуска по беременности и родам")
        return "Готово!"


class GetFile15(Message):
    def request(self):
        return "15"

    def response(self):
        self.server.upload_document(self.event,
                                    "documents/15_Zayavlenie_o_predostavlenii_otpuska_po_uhodu_za_rebenkom.doc",
                                    "Заявление о предоставлении отпуска по уходу за ребенком")
        return "Готово!"


class GetFile16(Message):
    def request(self):
        return "16"

    def response(self):
        self.server.upload_document(self.event,
                                    "documents/16_Zayavlenie_o_prodlenii_akademicheskogo_otpuska.doc",
                                    "Заявление о продлении академического отпуска")
        return "Готово!"


class GetFile17(Message):
    def request(self):
        return "17"

    def response(self):
        self.server.upload_document(self.event,
                                    "documents/17_Zayavlenie_o_vihode_iz_akademicheskogo_otpuska.doc",
                                    "Заявление о выходе из академического отпуска")
        return "Готово!"


class GetFile18(Message):
    def request(self):
        return "18"

    def response(self):
        self.server.upload_document(self.event,
                                    "documents/18__Zayavlenie_o_prikreplenii_dlya_sdachi_kandidatskih_ekzamenov_bez_osvoeniya_programm_aspiranturi.docx",
                                    "Заявление о прикреплении для сдачи кандидатских экзаменов без освоения программ аспирантуры")
        return "Готово!"


class GetFile19(Message):
    def request(self):
        return "19"

    def response(self):
        self.server.upload_document(self.event,
                                    "documents/19__Zayavlenie_o_prikreplenii_dlya_podgotovki_dissertacii_na_soiskanie_uchenoyi_stepeni_kandidata_nauk_bez_osvoeniya_programmi_aspiranturi.doc",
                                    "Заявление о прикреплении для подготовки диссертации на соискание ученой степени кандидата наук без освоения программы аспирантуры")
        return "Готово!"


class GetFile20(Message):
    def request(self):
        return "20"

    def response(self):
        self.server.upload_document(self.event,
                                    "documents/20_Zayavlenie_o_perevode_s_platnoyi_osnovi_obucheniya_na_byudjetnuyu.doc",
                                    "Заявление о переводе с платной основы обучения на бюджетную")
        return "Готово!"


class GetFile21(Message):
    def request(self):
        return "21"

    def response(self):
        self.server.upload_document(self.event,
                                    "documents/21_Zayavlenie_ob_apellyacii_ocenki._poluchennoyi_na_zaschite_nauchnogo_doklada.doc",
                                    "Заявление об апелляции оценки, полученной на защите научного доклада")
        return "Готово!"


class GetFile22(Message):
    def request(self):
        return "22"

    def response(self):
        self.server.upload_document(self.event,
                                    "documents/22_Zayavlenie_ob_apellyacii_ocenki._poluchennoyi_na_gosudarstvennom_itogovom_ekzamene.doc",
                                    "Заявление об апелляции оценки, полученной на государственном итоговом экзамене")
        return "Готово!"


class GetFile23(Message):
    def request(self):
        return "23"

    def response(self):
        self.server.upload_document(self.event,
                                    "documents/23_Zayavlenie_o_perezachtenii_kandidatskogo_ekzamena.docx",
                                    "Заявление о перезачтении кандидатского экзамена")
        return "Готово!"


class GetAllDocuments(Message):
    def request(self):
        return "список документов"

    def response(self):
        return "Введите номер документа:\n" \
               "1. Заявление о продлении срока промежуточной аттестации\n" \
               "2. Заявление о перезачтении дисциплин\n" \
               "3. Заявление об переводе из другого вуза в ПНИПУ для продолжения обучения по программе аспирантуры\n" \
               "4. Заявление о переходе с программы на программу ПНИПУ\n" \
               "5. Заявление о переводе на ускоренное обучение за счет повышения интенсивности освоения программы\n" \
               "6. Заявление о переводе на ускоренное обучение за счет перезачета ранее сданных дисциплин\n" \
               "7. Заявление об отчислении из ПНИПУ в связи с переводом для продолжения обучения в др.вузе\n" \
               "8. Заявление об отчислении из ПНИПУ по собственному желанию\n" \
               "9. Заявление о восстановлении в ПНИПУ\n" \
               "10. Заявление об апелляции оценки на вступительных экзаменах\n" \
               "11. Заявление о смене фамилии\n" \
               "12. Заявление о смене научного руководителя\n" \
               "13. Заявление о предоставлении академического отпуска\n" \
               "14. Заявление о предоставлении отпуска по беременности и родам\n" \
               "15. Заявление о предоставлении отпуска по уходу за ребенком\n" \
               "16. Заявление о продлении академического отпуска\n" \
               "17. Заявление о выходе из академического отпуска\n" \
               "18. Заявление о прикреплении для сдачи кандидатских экзаменов без освоения программ аспирантуры\n" \
               "19. Заявление о прикреплении для подготовки диссертации на соискание ученой степени кандидата наук без освоения программы аспирантуры\n" \
               "20. Заявление о переводе с платной основы обучения на бюджетную\n" \
               "21. Заявление об апелляции оценки, полученной на защите научного доклада\n" \
               "22. Заявление об апелляции оценки, полученной на государственном итоговом экзамене\n" \
               "23. Заявление о перезачтении кандидатского экзамена"

    
 
class GetKUG(Message):
    def request(self):
        return r"(календарный план)|(календарный график)"

    def response(self):
        return "Ваша форма обучения?" 


class GetKUGoch(Message):
    def request(self):
        return "очная"

    def response(self):
        self.server.upload_document(self.event,
                                    "documents/KUG_ochnoe.pdf",
                                    "Единый календарный учебный график очной формы обучения")
        return "Готово!"


class GetKUGzaoch(Message):
    def request(self):
        return "заочная"

    def response(self):
        self.server.upload_document(self.event,
                                    "documents/KUG_zaochnoe.pdf",
                                    "Единый календарный учебный график заочной формы обучения")
        return "Готово!"


class GetKUGoch_zaoch(Message):
    def request(self):
        return r"(очно-заочная)|(очно заочная)"

    def response(self):
        self.server.upload_document(self.event,
                                    "documents/KUG_ochno-zaochnoe.pdf",
                                    "Единый календарный учебный график очно-заочной формы обучения")
        return "Готово!"   
    
    
