from dataclasses import dataclass, field
import logging


_LOGGER = logging.getLogger(__name__)

@dataclass
class Status:
    status: str | None = None
    stato_stufa: int | None = None
    turbo_activation_timestamp: int | None = None
    scheduled_turn_off_timestamp: int | None = None
    is_crono_empty: bool | None = None
    is_ble_connected: bool | None = None
    sm_nome_app: str | None = None
    sm_vs_app: int | None = None
    mc_vs_app: str | None = None
    fase_op: str | None = None
    sub_fase_op: str | None = None
    mod_lav_att: str | None = None
    set_pot_man: int | None = None
    set_amb1: float | None = None
    set_amb2: float | None = None
    set_amb3: float | None = None
    set_vent_v1: int | None = None
    set_vent_v2: int | None = None
    set_vent_v3: int | None = None
    v_ven1_v0: int | None = None
    v_ven2_v0: int | None = None
    v_ven3_v0: int | None = None
    potenza_att: int | None = None
    index_vel_v1: int | None = None
    index_vel_v2: int | None = None
    index_vel_v3: int | None = None
    temp_amb_can1: float | None = None
    temp_amb_can2: float | None = None
    temp_amb_can3: float | None = None
    temp_amb_install: float | None = None 
    wifi_status: int | None = None
    silent_enabled: bool | None = None
    crono_enabled: bool | None = None
    sleep_enabled: bool | None = None
    clean_air_in_prog: bool | None = None
    clean_in_prog: bool | None = None
    power_enabled: bool | None = None
    silent: bool | None = None
    t_power: int | None = None
    att_eco: bool | None = None
    sens_liv_pellet: bool | None = None
    auto_pellet: int | None = None
    sens_liv_pel: bool | None = None
    pul_brac: bool | None = None
    ingr_amb: int | None = None
    rit_usc_standby: int | None = None
    rit_ing_standby: int | None = None
    ist_neg_amb: float | None = None
    ist_pos_amb: float | None = None
    ist_eco_neg_amb: float | None = None
    ist_eco_pos_amb: float | None = None
    com_es_car_coclea: bool | None = None
    t_car_pel_man: int | None = None
    pos_ric_pel: int | None = None
    pos_ric_flu: int | None = None
    anno: int | None = None
    mese: int | None = None
    giorno: int | None = None
    ore: int | None = None
    minuti: int | None = None
    secondi: int | None = None
    giorno_sett: int | None = None
    am_pm: bool | None = None
    pressione_pascal: int | None = None
    pressione: int | None = None
    pressione_imp: int | None = None
    act: bool | None = None
    act_acc: bool | None = None
    ore_prox_manut: int | None = None
    toni_buzz: int | None = None
    mod_ada_on: bool | None = None
    ssid_wifi: str | None = None
    sm_sn: str | None = None
    nome_banca_dati_sel: str | None = None
    cont_fine_pul: bool | None = None
    ing_term_amb1: bool | None = None
    description: str | None = None
    is_connected: bool | None = None
    is_in_error: bool | None = None
    status_timestamp: int | None = None
    last_stdt: int | None = None
    site_time_zone: str | None = None
    blocking_event_id: str | None = None
    pren_acc: bool | None = None
    umid_rel: float | None = None

    #first generation M1+ only fields
    pwd_wifi: str | None = None
    mac_wifi: str | None = None
    vs_remoto: str | None = None
    vs_wifi_home: str | None = None
    sm_vs_bootloader: str | None = None
    vs_ambient: str | None = None
    sondaWifi: int | None = None

    #hydro stove fields
    is_pump_active: bool | None = None
    power_caller: str | None = None
    ing_term_amb2: bool | None = None
    ing_term_amb3: bool | None = None
    est_inv: int | None = None
    pompa: int | None = None
    conf_imp: int | None = None
    temp_caldaia: float | None = None
    ingr_ntc2: int | None = None
    ingr_ntc3: int | None = None
    conf_rele_aux: int | None = None
    temp_NTC1: float | None = None
    temp_NTC2: float | None = None
    temp_NTC3: float | None = None
    temp_puffer: float | None = None
    term_puff: bool | None = None
    temp_bollitore: float | None = None
    term_boll: bool | None = None
    temp_sonda_est: float | None = None
    temp_sonda_acc: float | None = None
    temp_termocoppia1: float | None = None
    stato_valv: bool | None = None
    stato_exit_pomp_ext: bool | None = None
    temp_max_mand: float | None = None
    temp_min_circ_on: float | None = None
    set_puffer: float | None = None
    ist_neg_puffer: float | None = None
    ist_pos_puffer: float | None = None
    set_boiler: float | None = None
    ist_neg_boiler: float | None = None
    ist_pos_boiler: float | None = None
    set_cald: float | None = None
    ist_neg_cald: float | None = None
    ist_pos_cald: float | None = None
    set_san: float | None = None
    soglia_temp_cons_cald: float | None = None
    com_inv_pos_bruciatore: bool | None = None
    tempo_sleep: int | None = None
    temp_max_stufa_off: float | None = None
    temp_min_stufa_on: float | None = None
    is_config_valid: bool | None = None
    ingr_flux: float | None = None
    soglia_usc_temp: float | None = None

    unknown_fields: dict | None = None

    def __init__(self, json, from_mocked_response = False) -> None:
        if(from_mocked_response):
            for k, v in json.items():
                 setattr(self, k, v)
        else:
            if(json is not None and len(json) > 0):
                temp_unknown_fields = {}
                for key in json:
                    match key:
                        case "Status": self.status = json[key]
                        case "stato_stufa": self.stato_stufa = json[key]
                        case "TurboActivationTimestamp": self.turbo_activation_timestamp = json[key]
                        case "ScheduledTurnOffTimestamp": self.scheduled_turn_off_timestamp = json[key]
                        case "IsCronoEmpty": self.is_crono_empty = json[key]
                        case "IsBLEConnected": self.is_ble_connected = json[key]
                        case "sm_nome_app": self.sm_nome_app = json[key]
                        case "sm_vs_app": self.sm_vs_app = json[key]
                        case "mc_vs_app": self.mc_vs_app = json[key]
                        case "fase_op": self.fase_op = json[key]
                        case "sub_fase_op": self.sub_fase_op = json[key]
                        case "mod_lav_att": self.mod_lav_att = json[key]
                        case "set_pot_man": self.set_pot_man = json[key]
                        case "set_amb1": self.set_amb1 = json[key]
                        case "set_amb2": self.set_amb2 = json[key]
                        case "set_amb3": self.set_amb3 = json[key]
                        case "set_vent_v1": self.set_vent_v1 = json[key]
                        case "set_vent_v2": self.set_vent_v2 = json[key]
                        case "set_vent_v3": self.set_vent_v3 = json[key]
                        case "v_ven1_v0": self.v_ven1_v0 = json[key]
                        case "v_ven2_v0": self.v_ven2_v0 = json[key]
                        case "v_ven3_v0": self.v_ven3_v0 = json[key]
                        case "potenza_att": self.potenza_att = json[key]
                        case "index_vel_v1": self.index_vel_v1 = json[key]
                        case "index_vel_v2": self.index_vel_v2 = json[key]
                        case "index_vel_v3": self.index_vel_v3 = json[key]
                        case "temp_amb_can1": self.temp_amb_can1 = json[key]
                        case "temp_amb_can2": self.temp_amb_can2 = json[key]
                        case "temp_amb_can3": self.temp_amb_can3 = json[key]
                        case "temp_amb_install": self.temp_amb_install = json[key]
                        case "wifi_status": self.wifi_status = json[key]
                        case "silent_enabled": self.silent_enabled = json[key]
                        case "crono_enabled": self.crono_enabled = json[key]
                        case "sleep_enabled": self.sleep_enabled = json[key]
                        case "clean_air_in_prog": self.clean_air_in_prog = json[key]
                        case "clean_in_prog": self.clean_in_prog = json[key]
                        case "power_enabled": self.power_enabled = json[key]
                        case "silent": self.silent = json[key]
                        case "t_power": self.t_power = json[key]
                        case "att_eco": self.att_eco = json[key]
                        case "sens_liv_pellet": self.sens_liv_pellet = json[key]
                        case "auto_pellet": self.auto_pellet = json[key]
                        case "sens_liv_pel": self.sens_liv_pel = json[key]
                        case "pul_brac": self.pul_brac = json[key]
                        case "ingr_amb": self.ingr_amb = json[key]
                        case "rit_usc_standby": self.rit_usc_standby = json[key]
                        case "rit_ing_standby": self.rit_ing_standby = json[key]
                        case "ist_neg_amb": self.ist_neg_amb = json[key]
                        case "ist_pos_amb": self.ist_pos_amb = json[key]
                        case "ist_eco_neg_amb": self.ist_eco_neg_amb = json[key]
                        case "ist_eco_pos_amb": self.ist_eco_pos_amb = json[key]
                        case "com_es_car_coclea": self.com_es_car_coclea = json[key]
                        case "t_car_pel_man": self.t_car_pel_man = json[key]
                        case "pos_ric_pel": self.pos_ric_pel = json[key]
                        case "pos_ric_flu": self.pos_ric_flu = json[key]
                        case "anno": self.anno = json[key]
                        case "mese": self.mese = json[key]
                        case "giorno": self.giorno = json[key]
                        case "ore": self.ore = json[key]
                        case "minuti": self.minuti = json[key]
                        case "secondi": self.secondi = json[key]
                        case "giorno_sett": self.giorno_sett = json[key]
                        case "am_pm": self.am_pm = json[key]
                        case "pressione_pascal": self.pressione_pascal = json[key]
                        case "pressione": self.pressione = json[key]
                        case "pressione_imp": self.pressione_imp = json[key]
                        case "act": self.act = json[key]
                        case "act_acc": self.act_acc = json[key]
                        case "ore_prox_manut": self.ore_prox_manut = json[key]
                        case "toni_buzz": self.toni_buzz = json[key]
                        case "mod_ada_on": self.mod_ada_on = json[key]
                        case "SSID_wifi": self.ssid_wifi = json[key]
                        case "sm_sn": self.sm_sn = json[key]
                        case "nome_banca_dati_sel": self.nome_banca_dati_sel = json[key]
                        case "cont_fine_pul": self.cont_fine_pul = json[key]
                        case "ing_term_amb1": self.ing_term_amb1 = json[key]
                        case "Description": self.description = json[key]
                        case "IsConnected": self.is_connected = json[key]
                        case "IsInError": self.is_in_error = json[key]
                        case "StatusTimestamp": self.status_timestamp = json[key]
                        case "LastSTDT": self.last_stdt = json[key]
                        case "SiteTimeZone": self.site_time_zone = json[key]
                        case "BlockingEventId": self.blocking_event_id = json[key]
                        case "pren_acc" : self.pren_acc = json[key]
                        case "umid_rel" : self.umid_rel = json[key]


                        case "pwd_wifi": self.pwd_wifi = json[key]
                        case "mac_wifi": self.mac_wifi = json[key]
                        case "vs_remoto": self.vs_remoto = json[key]
                        case "vs_wifi_home": self.vs_wifi_home = json[key]
                        case "sm_vs_bootloader": self.sm_vs_bootloader = json[key]
                        case "vs_ambient": self.vs_ambient = json[key]
                        case "sondaWifi": self.sondaWifi = json[key]

                        case "IsPumpActive": self.is_pump_active = json[key]
                        case "power_caller": self.power_caller = json[key]
                        case "ing_term_amb2": self.ing_term_amb2 = json[key]
                        case "ing_term_amb3": self.ing_term_amb3 = json[key]
                        case "est_inv": self.est_inv = json[key]
                        case "pompa": self.pompa = json[key]
                        case "conf_imp": self.conf_imp = json[key]
                        case "temp_caldaia": self.temp_caldaia = json[key]
                        case "ingr_ntc2": self.ingr_ntc2 = json[key]
                        case "ingr_ntc3": self.ingr_ntc3 = json[key]
                        case "conf_rele_aux": self.conf_rele_aux = json[key]
                        case "temp_NTC1": self.temp_NTC1 = json[key]
                        case "temp_NTC2": self.temp_NTC2 = json[key]
                        case "temp_NTC3": self.temp_NTC3 = json[key]
                        case "temp_puffer": self.temp_puffer = json[key]
                        case "term_puff": self.term_puff = json[key]
                        case "temp_bollitore": self.temp_bollitore = json[key]
                        case "term_boll": self.term_boll = json[key]
                        case "temp_sonda_est": self.temp_sonda_est = json[key]
                        case "temp_sonda_acc": self.temp_sonda_acc = json[key]
                        case "temp_termocoppia1": self.temp_termocoppia1 = json[key]
                        case "stato_valv": self.stato_valv = json[key]
                        case "stato_exit_pomp_ext": self.stato_exit_pomp_ext = json[key]
                        case "temp_max_mand": self.temp_max_mand = json[key]
                        case "temp_min_circ_on": self.temp_min_circ_on = json[key]
                        case "set_puffer": self.set_puffer = json[key]
                        case "ist_neg_puffer": self.ist_neg_puffer = json[key]
                        case "ist_pos_puffer": self.ist_pos_puffer = json[key]
                        case "set_boiler": self.set_boiler = json[key]
                        case "ist_neg_boiler": self.ist_neg_boiler = json[key]
                        case "ist_pos_boiler": self.ist_pos_boiler = json[key]
                        case "set_cald": self.set_cald = json[key]
                        case "ist_neg_cald": self.ist_neg_cald = json[key]
                        case "ist_pos_cald": self.ist_pos_cald = json[key]
                        case "set_san": self.set_san = json[key]
                        case "soglia_temp_cons_cald": self.soglia_temp_cons_cald = json[key]
                        case "com_inv_pos_bruciatore": self.com_inv_pos_bruciatore = json[key]
                        case "tempo_sleep": self.tempo_sleep = json[key]
                        case "temp_max_stufa_off": self.temp_max_stufa_off = json[key]
                        case "temp_min_stufa_on": self.temp_min_stufa_on = json[key]
                        case "isConfigValid": self.is_config_valid = json[key]
                        case "ingr_flux": self.ingr_flux = json[key]
                        case "soglia_usc_temp": self.soglia_usc_temp = json[key]
                        case _ :
                            temp_unknown_fields[key] = json[key]
                            _LOGGER.warning(f"Unknown status property '{key}' received from API endpoint. If this happens, please make an issue on the github repository")
                if temp_unknown_fields:
                    self.unknown_fields = temp_unknown_fields

       
         