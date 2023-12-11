
TextoAlarme = '''

	(*Painel_Controle*)
	AlarmRecord[001](input:=PainelControle.Falha_EmergenciaLocal, reset:=reset, output=> Alarm_Matriz[01].00 );
	AlarmRecord[002](input:=PainelControle.Falha_EmergenciaSuperSEP, reset:= reset, output=> Alarm_Matriz[01].01 );
	AlarmRecord[003](input:=PainelControle.Falha_EmergenciaUHRV, reset:= reset, output=> Alarm_Matriz[01].02 );
	AlarmRecord[004](input:=PainelControle.Falha_EmergenciaUHLM, reset:= reset, output=> Alarm_Matriz[01].03 );
	(*AlarmRecord[005](input:=PainelControle.Reserva, reset:=reset, output=> Alarm_Matriz[01].04 );
	AlarmRecord[006](input:=PainelControle.Reserva, reset:=reset, output=> Alarm_Matriz[01].05 );
	AlarmRecord[007](input:=PainelControle.Reserva, reset:=reset, output=> Alarm_Matriz[01].06 );
	AlarmRecord[008](input:=PainelControle.Reserva, reset:=reset, output=> Alarm_Matriz[01].07 );
	AlarmRecord[009](input:=PainelControle.Reserva, reset:=reset, output=> Alarm_Matriz[01].08 );
	AlarmRecord[010](input:=PainelControle.Reserva, reset:=reset, output=> Alarm_Matriz[01].09 );
	AlarmRecord[011](input:=PainelControle.Reserva, reset:=reset, output=> Alarm_Matriz[01].10 );
	AlarmRecord[012](input:=PainelControle.Reserva, reset:=reset, output=> Alarm_Matriz[01].11 );
	AlarmRecord[013](input:=PainelControle.Reserva, reset:=reset, output=> Alarm_Matriz[01].12 );
	AlarmRecord[014](input:=PainelControle.Reserva, reset:=reset, output=> Alarm_Matriz[01].13 );
	AlarmRecord[015](input:=PainelControle.Reserva, reset:=reset, output=> Alarm_Matriz[01].14 );
	AlarmRecord[016](input:=PainelControle.Reserva, reset:=reset, output=> Alarm_Matriz[01].15 );*)




	(*Modo_Automatico*)
	AlarmRecord[017](input:= ModoAutomatico.Falha_UPtoUPGM, reset:= reset, output=> Alarm_Matriz[02].00 );
	AlarmRecord[018](input:= ModoAutomatico.Falha_UPGMtoUMD, reset:= reset, output=> Alarm_Matriz[02].01 );
	AlarmRecord[019](input:= ModoAutomatico.Falha_UMDtoUPS, reset:= reset, output=> Alarm_Matriz[02].02 );
	AlarmRecord[020](input:= ModoAutomatico.Falha_UPStoUS, reset:= reset, output=> Alarm_Matriz[02].03 );
	AlarmRecord[021](input:= ModoAutomatico.Falha_UStoUPS, reset:= reset, output=> Alarm_Matriz[02].04 );
	AlarmRecord[022](input:= ModoAutomatico.Falha_UPStoUMD, reset:= reset, output=> Alarm_Matriz[02].05 );
	AlarmRecord[023](input:= ModoAutomatico.Falha_UMDtoUPGM, reset:= reset, output=> Alarm_Matriz[02].06 );
	AlarmRecord[024](input:= ModoAutomatico.Falha_UPGMtoUP, reset:= reset, output=> Alarm_Matriz[02].07 );
	AlarmRecord[025](input:= ModoAutomatico.Falha_SequenciaIncompleta, reset:= reset, output=> Alarm_Matriz[02].08 );
	(*AlarmRecord[026](input:= ModoAutomatico.Reserva, reset:= reset, output=> Alarm_Matriz[02].09);*)
	(*AlarmRecord[027](input:= ModoAutomatico.Reserva, reset:= reset, output=> Alarm_Matriz[02].10);*)
	(*AlarmRecord[028](input:= ModoAutomatico.Reserva, reset:= reset, output=> Alarm_Matriz[02].11);*)
	(*AlarmRecord[029](input:= ModoAutomatico.Reserva, reset:= reset, output=> Alarm_Matriz[02].12);*)
	(*AlarmRecord[030](input:= ModoAutomatico.Reserva, reset:= reset, output=> Alarm_Matriz[02].13);*)
	(*AlarmRecord[031](input:= ModoAutomatico.Reserva, reset:= reset, output=> Alarm_Matriz[02].14);*)
	(*AlarmRecord[032](input:= ModoAutomatico.Reserva, reset:= reset, output=> Alarm_Matriz[02].15);*)



	(*c_Controle_Potencia*)
	AlarmRecord[033](input:= CtrlP.Falha_Alarme, reset:= reset, output=> Alarm_Matriz[03].00 );
	AlarmRecord[034](input:= CtrlP.Falha_Trip, reset:= reset, output=> Alarm_Matriz[03].01 );
	(*AlarmRecord[035](input:= CtrlP.Reserva, reset:= reset, output=> Alarm_Matriz[03].02);
	AlarmRecord[036](input:= CtrlP.Reserva, reset:= reset, output=> Alarm_Matriz[03].03 );		
	AlarmRecord[037](input:= CtrlP.Reserva, reset:= reset, output=> Alarm_Matriz[03].04 );
	AlarmRecord[038](input:= CtrlP.Reserva, reset:= reset, output=> Alarm_Matriz[03].05 );
	AlarmRecord[039](input:= CtrlP.Reserva, reset:= reset, output=> Alarm_Matriz[03].06 );
	AlarmRecord[040](input:= CtrlP.Reserva, reset:= reset, output=> Alarm_Matriz[03].07 );
	AlarmRecord[041](input:= CtrlP.Reserva, reset:= reset, output=> Alarm_Matriz[03].08 );
	AlarmRecord[042](input:= CtrlP.Reserva, reset:= reset, output=> Alarm_Matriz[03].09 );
	AlarmRecord[043](input:= CtrlP.Reserva, reset:= reset, output=> Alarm_Matriz[03].10 );
	AlarmRecord[044](input:= CtrlP.Reserva, reset:= reset, output=> Alarm_Matriz[03].11 );
	AlarmRecord[045](input:= CtrlP.Reserva, reset:= reset, output=> Alarm_Matriz[03].12 );
	AlarmRecord[046](input:= CtrlP.Reserva, reset:= reset, output=> Alarm_Matriz[03].13 );
	AlarmRecord[047](input:= CtrlP.Reserva, reset:= reset, output=> Alarm_Matriz[03].15 );
	AlarmRecord[048](input:= CtrlP.Reserva, reset:= reset, output=> Alarm_Matriz[03].14 );*)



	(*d_UHLM*)
	AlarmRecord[049](input:= UHLM_Monitor_TrocCalor.Alarme, reset:= reset, output=> Alarm_Matriz[04].00);
	AlarmRecord[050](input:= UHLM_Monitor_TrocCalor.Trip, reset:= reset, output=> Alarm_Matriz[04].01);
	AlarmRecord[051](input:= UHLM_Monitor_PressostatoLinha.Alarme, reset:= reset, output=> Alarm_Matriz[04].02);
	AlarmRecord[052](input:= UHLM_Monitor_PressostatoLinha.Trip, reset:= reset, output=> Alarm_Matriz[04].03);
	AlarmRecord[053](input:= UHLM_Monitor_NiveOleoMaximo.Alarme, reset:= reset, output=> Alarm_Matriz[04].04);
	AlarmRecord[054](input:= UHLM_Monitor_NiveOleoMaximo.Trip, reset:= reset, output=> Alarm_Matriz[04].05);
	AlarmRecord[055](input:= UHLM_Monitor_NiveOleoMinimo.Alarme, reset:= reset, output=> Alarm_Matriz[04].06);
	AlarmRecord[056](input:= UHLM_Monitor_NiveOleoMinimo.Trip, reset:= reset, output=> Alarm_Matriz[04].07);
	AlarmRecord[057](input:= UHLM_Monitor_FiltroOleo01.Alarme, reset:= reset, output=> Alarm_Matriz[04].08);
	AlarmRecord[058](input:= UHLM_Monitor_FiltroOleo01.Trip, reset:= reset, output=> Alarm_Matriz[04].09);
	AlarmRecord[059](input:= UHLM_Monitor_FiltroOleo02.Alarme, reset:= reset, output=> Alarm_Matriz[04].10);
	AlarmRecord[060](input:= UHLM_Monitor_FiltroOleo02.Trip, reset:= reset, output=> Alarm_Matriz[04].11);
	AlarmRecord[061](input:= UHLM_Monitor_FiltroOleo03.Alarme, reset:= reset, output=> Alarm_Matriz[04].12);
	AlarmRecord[062](input:= UHLM_Monitor_FiltroOleo03.Trip, reset:= reset, output=> Alarm_Matriz[04].13);
	AlarmRecord[063](input:= UHLM_Monitor_FiltroOleo04.Alarme, reset:= reset, output=> Alarm_Matriz[04].14);
	AlarmRecord[064](input:= UHLM_Monitor_FiltroOleo04.Trip, reset:= reset, output=> Alarm_Matriz[04].15);


	AlarmRecord[065](input:= UHLM_Monitor_FiltroOleo05.Alarme, reset:= reset, output=> Alarm_Matriz[05].00);
	AlarmRecord[066](input:= UHLM_Monitor_FiltroOleo05.Trip, reset:= reset, output=> Alarm_Matriz[05].01);
	AlarmRecord[067](input:= UHLM_Monitor_FluxoOleo01.Alarme, reset:= reset, output=> Alarm_Matriz[05].02);
	AlarmRecord[068](input:= UHLM_Monitor_FluxoOleo01.Trip, reset:= reset, output=> Alarm_Matriz[05].03);
	AlarmRecord[069](input:= UHLM_Monitor_FluxoOleo02.Alarme, reset:= reset, output=> Alarm_Matriz[05].04);
	AlarmRecord[070](input:= UHLM_Monitor_FluxoOleo02.Trip, reset:= reset, output=> Alarm_Matriz[05].05);
	AlarmRecord[071](input:= UHLM_Monitor_FluxoOleo03.Alarme, reset:= reset, output=> Alarm_Matriz[05].06);
	AlarmRecord[072](input:= UHLM_Monitor_FluxoOleo03.Trip, reset:= reset, output=> Alarm_Matriz[05].07);
	AlarmRecord[073](input:= UHLM_Monitor_FluxoOleo04.Alarme, reset:= reset, output=> Alarm_Matriz[05].08);
	AlarmRecord[074](input:= UHLM_Monitor_FluxoOleo04.Trip, reset:= reset, output=> Alarm_Matriz[05].09);
	AlarmRecord[075](input:= UHLM_Monitor_FluxoOleo05.Alarme, reset:= reset, output=> Alarm_Matriz[05].10);
	AlarmRecord[076](input:= UHLM_Monitor_FluxoOleo05.Trip, reset:= reset, output=> Alarm_Matriz[05].11);
	AlarmRecord[077](input:= UHLM_Monitor_VazaoOleo.Alarme, reset:= reset, output=> Alarm_Matriz[05].12);
	AlarmRecord[078](input:= UHLM_Monitor_VazaoOleo.Trip, reset:= reset, output=> Alarm_Matriz[05].13);
	AlarmRecord[079](input:= UHLM_Bomba01.Falha_Acionamento, reset:= reset, output=> Alarm_Matriz[05].14);
	AlarmRecord[080](input:= UHLM_Bomba01.Falha_Trip, reset:= reset, output=> Alarm_Matriz[05].15);


	(*AlarmRecord[081](input:= UHLM_Bomba02.Falha_Acionamento, reset:= reset, output=> Alarm_Matriz[06].00);
	AlarmRecord[082](input:= UHLM_Bomba02.Falha_Trip, reset:= reset, output=> Alarm_Matriz[06].01);
	AlarmRecord[083](input:= UHLM_Bomba03.Falha_Acionamento, reset:= reset, output=> Alarm_Matriz[06].02);
	AlarmRecord[084](input:= UHLM_Bomba03.Falha_Trip, reset:= reset, output=> Alarm_Matriz[06.03);
	AlarmRecord[085](input:= UHLM_Bomba04.Falha_Acionamento, reset:= reset, output=> Alarm_Matriz[06].04);
	AlarmRecord[086](input:= UHLM_Bomba04.Falha_Trip, reset:= reset, output=> Alarm_Matriz[06].05);
	AlarmRecord[087](input:= UHLM_Bomba05.Falha_Acionamento, reset:= reset, output=> Alarm_Matriz[06].06);
	AlarmRecord[088](input:= UHLM_Bomba05.Falha_Trip, reset:= reset, output=> Alarm_Matriz[06].07);*)
	AlarmRecord[089](input:= UHLM_ResAquec_Monitor_Bomba.Alarme, reset:= reset, output=> Alarm_Matriz[06].08);
	AlarmRecord[090](input:= UHLM_ResAquec_Monitor_Bomba.Trip, reset:= reset, output=> Alarm_Matriz[06].09);
	AlarmRecord[091](input:= UHLM_ResAquec_Monitor_DjMotor.Alarme, reset:= reset, output=> Alarm_Matriz[06].10);
	AlarmRecord[092](input:= UHLM_ResAquec_Monitor_DjMotor.Trip, reset:= reset, output=> Alarm_Matriz[06].11);
	(*AlarmRecord[093](input:= UHLM.Reserva, reset:= reset, output=> Alarm_Matriz[06].12);
	AlarmRecord[094](input:= UHLM.Reserva, reset:= reset, output=> Alarm_Matriz[06].13);
	AlarmRecord[095](input:= UHLM.Reserva, reset:= reset, output=> Alarm_Matriz[06].14);
	AlarmRecord[096](input:= UHLM.Reserva, reset:= reset, output=> Alarm_Matriz[06].15);

	AlarmRecord[097](input:= UHLM.Reserva, reset:= reset, output=> Alarm_Matriz[07].00);
	AlarmRecord[098](input:= UHLM.Reserva, reset:= reset, output=> Alarm_Matriz[07].01);
	AlarmRecord[099](input:= UHLM.Reserva, reset:= reset, output=> Alarm_Matriz[07].02);
	AlarmRecord[100](input:= UHLM.Reserva, reset:= reset, output=> Alarm_Matriz[07.03);
	AlarmRecord[101](input:= UHLM.Reserva, reset:= reset, output=> Alarm_Matriz[07].04);
	AlarmRecord[102](input:= UHLM.Reserva, reset:= reset, output=> Alarm_Matriz[07].05);
	AlarmRecord[103](input:= UHLM.Reserva, reset:= reset, output=> Alarm_Matriz[07].06);
	AlarmRecord[104](input:= UHLM.Reserva, reset:= reset, output=> Alarm_Matriz[07].07);
	AlarmRecord[105](input:= UHLM.Reserva, reset:= reset, output=> Alarm_Matriz[07].08);
	AlarmRecord[106](input:= UHLM.Reserva, reset:= reset, output=> Alarm_Matriz[07].09);
	AlarmRecord[107](input:= UHLM.Reserva, reset:= reset, output=> Alarm_Matriz[07].10);
	AlarmRecord[108](input:= UHLM.Reserva, reset:= reset, output=> Alarm_Matriz[07].11);
	AlarmRecord[109](input:= UHLM.Reserva, reset:= reset, output=> Alarm_Matriz[07].12);
	AlarmRecord[110](input:= UHLM.Reserva, reset:= reset, output=> Alarm_Matriz[07].13);
	AlarmRecord[111](input:= UHLM.Reserva, reset:= reset, output=> Alarm_Matriz[07].14);
	AlarmRecord[112](input:= UHLM.Reserva, reset:= reset, output=> Alarm_Matriz[07].15);*)

	(*e_UHRV_Hacker*)
	AlarmRecord[113](input:= UHRV_Monitor_Pressurizacao.Alarme, reset:= reset, output=> Alarm_Matriz[08].00 );
	AlarmRecord[114](input:= UHRV_Monitor_Pressurizacao.Trip, reset:= reset, output=> Alarm_Matriz[08].01 );
	AlarmRecord[115](input:= UHRV_Monitor_Pressao.Alarme, reset:= reset, output=> Alarm_Matriz[08].02 );
	AlarmRecord[116](input:= UHRV_Monitor_Pressao.Trip, reset:= reset, output=> Alarm_Matriz[08].03 );
	AlarmRecord[117](input:= UHRV_Monitor_Pressostato.Alarme, reset:= reset, output=> Alarm_Matriz[08].04 );
	AlarmRecord[118](input:= UHRV_Monitor_Pressostato.Trip, reset:= reset, output=> Alarm_Matriz[08].05);
	AlarmRecord[119](input:= UHRV_Monitor_NiveOleoMaximo.Alarme, reset:= reset, output=> Alarm_Matriz[08].06 );
	AlarmRecord[120](input:= UHRV_Monitor_NiveOleoMaximo.Trip, reset:= reset, output=> Alarm_Matriz[08].07 );
	AlarmRecord[121](input:= UHRV_Monitor_NiveOleoMinimo.Alarme, reset:= reset, output=> Alarm_Matriz[08].08 );
	AlarmRecord[122](input:= UHRV_Monitor_NiveOleoMinimo.Trip, reset:= reset, output=> Alarm_Matriz[08].09 );
	AlarmRecord[123](input:= UHRV_Monitor_FiltroOleo01.Alarme, reset:= reset, output=> Alarm_Matriz[08].10 );
	AlarmRecord[124](input:= UHRV_Monitor_FiltroOleo01.Trip, reset:= reset, output=> Alarm_Matriz[08].11 );
	AlarmRecord[125](input:= UHRV_Monitor_FiltroOleo02.Alarme, reset:= reset, output=> Alarm_Matriz[08].12 );
	AlarmRecord[126](input:= UHRV_Monitor_FiltroOleo02.Trip, reset:= reset, output=> Alarm_Matriz[08].13 );
	AlarmRecord[127](input:= UHRV_Monitor_FiltroOleo03.Alarme, reset:= reset, output=> Alarm_Matriz[08].14 );
	AlarmRecord[128](input:= UHRV_Monitor_FiltroOleo03.Trip, reset:= reset, output=> Alarm_Matriz[08].15 );
	AlarmRecord[129](input:= UHRV_Monitor_FiltroOleo04.Alarme, reset:= reset, output=> Alarm_Matriz[09].00 );
	AlarmRecord[130](input:= UHRV_Monitor_FiltroOleo04.Trip, reset:= reset, output=> Alarm_Matriz[09].01 );
	AlarmRecord[131](input:= UHRV_Monitor_FiltroOleo05.Alarme, reset:= reset, output=> Alarm_Matriz[09].02 );
	AlarmRecord[132](input:= UHRV_Monitor_FiltroOleo05.Trip, reset:= reset, output=> Alarm_Matriz[09].03 );
	AlarmRecord[133](input:= UHRV_Monitor_FiltroPressao01.Alarme, reset:= reset, output=> Alarm_Matriz[09].04 );
	AlarmRecord[134](input:= UHRV_Monitor_FiltroPressao01.Trip, reset:= reset, output=> Alarm_Matriz[09].05 );
	AlarmRecord[135](input:= UHRV_Monitor_FiltroPressao02.Alarme, reset:= reset, output=> Alarm_Matriz[09].06 );
	AlarmRecord[136](input:= UHRV_Monitor_FiltroPressao02.Trip, reset:= reset, output=> Alarm_Matriz[09].07 );
	AlarmRecord[137](input:=  UHRV_Monitor_FiltroPressao03.Alarme, reset:= reset, output=> Alarm_Matriz[09].08 );
	AlarmRecord[138](input:= UHRV_Monitor_FiltroPressao03.Trip, reset:= reset, output=> Alarm_Matriz[09].09 );
	AlarmRecord[139](input:= UHRV_Monitor_FiltroPressao04.Alarme, reset:= reset, output=> Alarm_Matriz[09].10 );
	AlarmRecord[140](input:= UHRV_Monitor_FiltroPressao04.Trip, reset:= reset, output=> Alarm_Matriz[09].11 );
	AlarmRecord[141](input:= UHRV_Monitor_FiltroPressao05.Alarme, reset:= reset, output=> Alarm_Matriz[09].12 );
	AlarmRecord[142](input:= UHRV_Monitor_FiltroPressao05.Trip, reset:= reset, output=> Alarm_Matriz[09].13 );
	AlarmRecord[143](input:= UHRV_Bomba01.Falha_Acionamento, reset:= reset, output=> Alarm_Matriz[09].14 );
	AlarmRecord[144](input:= UHRV_Bomba01.Falha_Trip, reset:= reset, output=> Alarm_Matriz[09].15 );
	(*AlarmRecord[145](input:= UHRV_Bomba02.Falha_Acionamento, reset:= reset, output=> Alarm_Matriz[10].00 );
	AlarmRecord[146](input:= UHRV_Bomba02.Falha_Trip, reset:= reset, output=> Alarm_Matriz[10].01 );
	AlarmRecord[147](input:= UHRV_Bomba03.Falha_Acionamento, reset:= reset, output=> Alarm_Matriz[10.02 );
	AlarmRecord[148](input:= UHRV_Bomba03.Falha_Trip, reset:= reset, output=> Alarm_Matriz[10].03 );
	AlarmRecord[149](input:= UHRV_Bomba04.Falha_Acionamento, reset:= reset, output=> Alarm_Matriz[10].04 );
	AlarmRecord[150](input:= UHRV_Bomba04.Falha_Trip, reset:= reset, output=> Alarm_Matriz[10].05 );
	AlarmRecord[151](input:= UHRV_Bomba05.Falha_Acionamento, reset:= reset, output=> Alarm_Matriz[10].06 );
	AlarmRecord[152](input:= UHRV_Bomba05.Falha_Trip, reset:= reset, output=> Alarm_Matriz[10].07 );
	AlarmRecord[153](input:= UHRV.Reserva, reset:= reset, output=> Alarm_Matriz[10].08 );
	AlarmRecord[154](input:= UHRV.Reserva, reset:= reset, output=> Alarm_Matriz[10].09 );
	AlarmRecord[155](input:= UHRV.Reserva, reset:= reset, output=> Alarm_Matriz[10].10 );
	AlarmRecord[156](input:= UHRV.Reserva, reset:= reset, output=> Alarm_Matriz[10].11 );
	AlarmRecord[157](input:= UHRV.Reserva, reset:= reset, output=> Alarm_Matriz[10].12 );
	AlarmRecord[158](input:= UHRV.Reserva, reset:= reset, output=> Alarm_Matriz[10].13 );
	AlarmRecord[159](input:= UHRV.Reserva, reset:= reset, output=> Alarm_Matriz[10].14 );
	AlarmRecord[160](input:= UHRV.Reserva, reset:= reset, output=> Alarm_Matriz[10].15 );
	AlarmRecord[161](input:= UHRV.Reserva, reset:= reset, output=> Alarm_Matriz[11].00 );
	AlarmRecord[162](input:= UHRV.Reserva, reset:= reset, output=> Alarm_Matriz[11].01 );
	AlarmRecord[163](input:= UHRV.Reserva, reset:= reset, output=> Alarm_Matriz[11.02 );
	AlarmRecord[164](input:= UHRV.Reserva, reset:= reset, output=> Alarm_Matriz[11].03 );
	AlarmRecord[165](input:= UHRV.Reserva, reset:= reset, output=> Alarm_Matriz[11].04 );
	AlarmRecord[166](input:= UHRV.Reserva, reset:= reset, output=> Alarm_Matriz[11].05 );
	AlarmRecord[167](input:= UHRV.Reserva, reset:= reset, output=> Alarm_Matriz[11].06 );
	AlarmRecord[168](input:= UHRV.Reserva, reset:= reset, output=> Alarm_Matriz[11].07 );
	AlarmRecord[169](input:= UHRV.Reserva, reset:= reset, output=> Alarm_Matriz[11].08 );
	AlarmRecord[170](input:= UHRV.Reserva, reset:= reset, output=> Alarm_Matriz[11].09 );
	AlarmRecord[171](input:= UHRV.Reserva, reset:= reset, output=> Alarm_Matriz[11].10 );
	AlarmRecord[172](input:= UHRV.Reserva, reset:= reset, output=> Alarm_Matriz[11].11 );
	AlarmRecord[173](input:= UHRV.Reserva, reset:= reset, output=> Alarm_Matriz[11].12 );
	AlarmRecord[174](input:= UHRV.Reserva, reset:= reset, output=> Alarm_Matriz[11].13 );
	AlarmRecord[175](input:= UHRV.Reserva, reset:= reset, output=> Alarm_Matriz[11].14 );
	AlarmRecord[176](input:= UHRV.Reserva, reset:= reset, output=> Alarm_Matriz[11].15 );*)

	(*f_Sist_Filtragem_Agua*)
	AlarmRecord[177](input:=SFA_Bomba01.Falha_Acionamento, reset:= reset, output=> Alarm_Matriz[12].00);
	AlarmRecord[178](input:=SFA_Bomba01.Falha_Trip, reset:= reset, output=> Alarm_Matriz[12].01);
	AlarmRecord[179](input:=SFA_Monitor.Alarme, reset:= reset, output=> Alarm_Matriz[12].02);
	AlarmRecord[180](input:=SFA_MonitoR.Trip, reset:= reset, output=> Alarm_Matriz[12].03);
	(*AlarmRecord[181](input:=SFA.Reserva, reset:= reset, output=> Alarm_Matriz[12].04);
	AlarmRecord[182](input:=SFA.Reserva, reset:= reset, output=> Alarm_Matriz[12].05);
	AlarmRecord[183](input:=SFA.Reserva, reset:= reset, output=> Alarm_Matriz[12].06);
	AlarmRecord[184](input:=SFA.Reserva, reset:= reset, output=> Alarm_Matriz[12].07);
	AlarmRecord[185](input:=SFA.Reserva, reset:= reset, output=> Alarm_Matriz[12].08);
	AlarmRecord[186](input:=SFA.Reserva, reset:= reset, output=> Alarm_Matriz[12].09);
	AlarmRecord[187](input:=SFA.Reserva, reset:= reset, output=> Alarm_Matriz[12].10);
	AlarmRecord[188](input:=SFA.Reserva, reset:= reset, output=> Alarm_Matriz[12].11);
	AlarmRecord[189](input:=SFA.Reserva, reset:= reset, output=> Alarm_Matriz[12].12);
	AlarmRecord[190](input:=SFA.Reserva, reset:= reset, output=> Alarm_Matriz[12].13);
	AlarmRecord[191](input:=SFA.Reserva, reset:= reset, output=> Alarm_Matriz[12].14);
	AlarmRecord[192](input:=SFA.Reserva, reset:= reset, output=> Alarm_Matriz[12].15)*)

	(*g_Turbina*)
	AlarmRecord[193](input:=Turbina_Monitor_Sensores.Alarme, reset:= reset, output=> Alarm_Matriz[13].00 );
	AlarmRecord[194](input:=Turbina_Monitor_Sensores.Trip, reset:= reset, output=> Alarm_Matriz[13].01 );
	AlarmRecord[195](input:=Turbina_Monitor_Equalizacao.Alarme, reset:= reset, output=> Alarm_Matriz[13].02 );
	AlarmRecord[196](input:=Turbina_Monitor_Equalizacao.Trip, reset:= reset, output=> Alarm_Matriz[13].03 );
	(*AlarmRecord[197](input:=Turbina.Reserva, reset:= reset, output=> Alarm_Matriz[13].04 );
	AlarmRecord[198](input:=Turbina.Reserva, reset:= reset, output=> Alarm_Matriz[13].05 );
	AlarmRecord[199](input:=Turbina.Reserva, reset:= reset, output=> Alarm_Matriz[13].06 );
	AlarmRecord[200](input:=Turbina.Reserva, reset:= reset, output=> Alarm_Matriz[13].07 );
	AlarmRecord[201](input:=Turbina.Reserva, reset:= reset, output=> Alarm_Matriz[13].08 );
	AlarmRecord[202](input:=Turbina.Reserva, reset:= reset, output=> Alarm_Matriz[13].09 );
	AlarmRecord[203](input:=Turbina.Reserva, reset:= reset, output=> Alarm_Matriz[13].10 );
	AlarmRecord[204](input:=Turbina.Reserva, reset:= reset, output=> Alarm_Matriz[13].11 );
	AlarmRecord[205](input:=Turbina.Reserva, reset:= reset, output=> Alarm_Matriz[13].12 );
	AlarmRecord[206](input:=Turbina.Reserva, reset:= reset, output=> Alarm_Matriz[13].13 );
	AlarmRecord[207](input:=Turbina.Reserva, reset:= reset, output=> Alarm_Matriz[13].14 );
	AlarmRecord[208](input:=Turbina.Reserva, reset:= reset, output=> Alarm_Matriz[13].15 );*)

	(*g_ByPass*)
	AlarmRecord[209](input:=Bypass_Monitor_Abertura.Alarme, reset:= reset, output=> Alarm_Matriz[14].00 );
	AlarmRecord[210](input:=Bypass_Monitor_Abertura.Trip, reset:= reset, output=> Alarm_Matriz[14].01 );
	AlarmRecord[211](input:=Bypass_Monitor_Fechamento.Alarme, reset:= reset, output=> Alarm_Matriz[14].02 );
	AlarmRecord[212](input:=Bypass_Monitor_Fechamento.Trip, reset:= reset, output=> Alarm_Matriz[14].03 );
	AlarmRecord[213](input:=Bypass_Monitor_Inconsistencia.Alarme, reset:= reset, output=> Alarm_Matriz[14].04 );
	AlarmRecord[214](input:=Bypass_Monitor_Inconsistencia.Trip, reset:= reset, output=> Alarm_Matriz[14].05 );
	(*AlarmRecord[215](input:=Bypass.Reserva, reset:= reset, output=> Alarm_Matriz[14].06 );
	AlarmRecord[216](input:=Bypass.Reserva, reset:= reset, output=> Alarm_Matriz[14].07 );
	AlarmRecord[217](input:=Bypass.Reserva, reset:= reset, output=> Alarm_Matriz[14].08 );
	AlarmRecord[218](input:=Bypass.Reserva, reset:= reset, output=> Alarm_Matriz[14].09 );
	AlarmRecord[219](input:=Bypass.Reserva, reset:= reset, output=> Alarm_Matriz[14].10 );
	AlarmRecord[220](input:=Bypass.Reserva, reset:= reset, output=> Alarm_Matriz[14].11 );
	AlarmRecord[221](input:=Bypass.Reserva, reset:= reset, output=> Alarm_Matriz[14].12 );
	AlarmRecord[222](input:=Bypass.Reserva, reset:= reset, output=> Alarm_Matriz[14].13 );
	AlarmRecord[223](input:=Bypass.Reserva, reset:= reset, output=> Alarm_Matriz[14].14 );
	AlarmRecord[224](input:=Bypass.Reserva, reset:= reset, output=> Alarm_Matriz[14].15 );*)

	(*g_Valv_Borboleta*)
	AlarmRecord[225](input:=Borboleta_Monitor_Seguranca.Alarme, reset:= reset, output=> Alarm_Matriz[15].00 );
	AlarmRecord[226](input:=Borboleta_Monitor_Seguranca.Trip, reset:= reset, output=> Alarm_Matriz[15].01 );
	AlarmRecord[227](input:=Borboleta_Monitor_Abertura.Alarme, reset:= reset, output=> Alarm_Matriz[15].02 );
	AlarmRecord[228](input:=Borboleta_Monitor_Abertura.Trip, reset:= reset, output=> Alarm_Matriz[15].03 );
	AlarmRecord[229](input:=Borboleta_Monitor_Fechamento.Alarme, reset:= reset, output=> Alarm_Matriz[15].04 );
	AlarmRecord[230](input:=Borboleta_Monitor_Fechamento.Trip, reset:= reset, output=> Alarm_Matriz[15].05 );
	AlarmRecord[231](input:=Borboleta_Monitor_Cracking.Alarme, reset:= reset, output=> Alarm_Matriz[15].06 );
	AlarmRecord[232](input:=Borboleta_Monitor_Cracking.Trip, reset:= reset, output=> Alarm_Matriz[15].07 );
	AlarmRecord[233](input:=Borboleta_Monitor_Reposicao.Alarme, reset:= reset, output=> Alarm_Matriz[15].08 );
	AlarmRecord[234](input:=Borboleta_Monitor_Reposicao.Trip, reset:= reset, output=> Alarm_Matriz[15].09 );
	AlarmRecord[235](input:=Borboleta_Monitor_Inconsistencia.Alarme, reset:= reset, output=> Alarm_Matriz[15].10 );
	AlarmRecord[236](input:=Borboleta_Monitor_Inconsistencia.Trip, reset:= reset, output=> Alarm_Matriz[15].11 );
	(*AlarmRecord[237](input:=Borboleta.Reserva, reset:= reset, output=> Alarm_Matriz[15].12 );
	AlarmRecord[238](input:=Borboleta.Reserva, reset:= reset, output=> Alarm_Matriz[15].13 );
	AlarmRecord[239](input:=Borboleta.Reserva, reset:= reset, output=> Alarm_Matriz[15].14 );
	AlarmRecord[240](input:=Borboleta.Reserva, reset:= reset, output=> Alarm_Matriz[15].15 );*)

	(*h_Reg_Velocidade*)
	AlarmRecord[241](input:=RegV_Monitor.Alarme, reset:= reset, output=> Alarm_Matriz[16].00 );
	AlarmRecord[242](input:=RegV_Monitor.Trip, reset:= reset, output=> Alarm_Matriz[16].01 );
	AlarmRecord[243](input:=RegV_Monitor_Regulador.Alarme, reset:= reset, output=> Alarm_Matriz[16].02 );
	AlarmRecord[244](input:=RegV_Monitor_Regulador.Trip, reset:= reset, output=> Alarm_Matriz[16].03 );
	AlarmRecord[245](input:=RegV_Monitor_Sobrevelocidade.Alarme, reset:= reset, output=> Alarm_Matriz[16].04 );
	AlarmRecord[246](input:=RegV_Monitor_Sobrevelocidade.Trip, reset:= reset, output=> Alarm_Matriz[16].05 );
	AlarmRecord[247](input:=RegV_Monitor_Seguranca.Alarme, reset:= reset, output=> Alarm_Matriz[16].06 );
	AlarmRecord[248](input:=RegV_Monitor_Seguranca.Trip, reset:= reset, output=> Alarm_Matriz[16].07 );
	AlarmRecord[249](input:=RegV_Monitor_Encoder.Alarme, reset:= reset, output=> Alarm_Matriz[16].08 );
	AlarmRecord[250](input:=RegV_Monitor_Encoder.Trip, reset:= reset, output=> Alarm_Matriz[16].09 );
	AlarmRecord[251](input:=RegV_Monitor_TransdutorPosicao.Alarme, reset:= reset, output=> Alarm_Matriz[16].10 );
	AlarmRecord[252](input:=RegV_Monitor_TransdutorPosicao.Trip, reset:= reset, output=> Alarm_Matriz[16].11 );
	AlarmRecord[253](input:=RegV_Monitor_Rotor.Alarme, reset:= reset, output=> Alarm_Matriz[16].12 );
	AlarmRecord[254](input:=RegV_Monitor_Rotor.Trip, reset:= reset, output=> Alarm_Matriz[16].13 );
	(*AlarmRecord[255](input:=RegV.Reserva, reset:= reset, output=> Alarm_Matriz[16].14 );
	AlarmRecord[256](input:=RegV.Reserva, reset:= reset, output=> Alarm_Matriz[16].15 );
	AlarmRecord[257](input:=RegV.Reserva, reset:= reset, output=> Alarm_Matriz[17].00 );
	AlarmRecord[258](input:=RegV.Reserva, reset:= reset, output=> Alarm_Matriz[17].01 );
	AlarmRecord[259](input:=RegV.Reserva, reset:= reset, output=> Alarm_Matriz[17].02 );
	AlarmRecord[260](input:=RegV.Reserva, reset:= reset, output=> Alarm_Matriz[17].03 );
	AlarmRecord[261](input:=RegV.Reserva, reset:= reset, output=> Alarm_Matriz[17].04 );
	AlarmRecord[262](input:=RegV.Reserva, reset:= reset, output=> Alarm_Matriz[17].05 );
	AlarmRecord[263](input:=RegV.Reserva, reset:= reset, output=> Alarm_Matriz[17].06 );
	AlarmRecord[264](input:=RegV.Reserva, reset:= reset, output=> Alarm_Matriz[17].07 );
	AlarmRecord[265](input:=RegV.Reserva, reset:= reset, output=> Alarm_Matriz[17].08 );
	AlarmRecord[266](input:=RegV.Reserva, reset:= reset, output=> Alarm_Matriz[17].09 );
	AlarmRecord[267](input:=RegV.Reserva, reset:= reset, output=> Alarm_Matriz[17].10 );
	AlarmRecord[268](input:=RegV.Reserva, reset:= reset, output=> Alarm_Matriz[17].11 );
	AlarmRecord[269](input:=RegV.Reserva, reset:= reset, output=> Alarm_Matriz[17].12 );
	AlarmRecord[270](input:=RegV.Reserva, reset:= reset, output=> Alarm_Matriz[17].13 );
	AlarmRecord[271](input:=RegV.Reserva, reset:= reset, output=> Alarm_Matriz[17].14 );
	AlarmRecord[272](input:=RegV.Reserva, reset:= reset, output=> Alarm_Matriz[17].15 );*)

	(*i_Reg_Tensao*)
	AlarmRecord[273](input:=RegT_Monitor.Alarme, reset:= reset, output=> Alarm_Matriz[18].00 );
	AlarmRecord[274](input:=RegT_Monitor.Trip, reset:= reset, output=> Alarm_Matriz[18].01 );
	AlarmRecord[275](input:=RegT_Monitor_FusivelTrafo.Alarme, reset:= reset, output=> Alarm_Matriz[18].02 );
	AlarmRecord[276](input:=RegT_Monitor_FusivelTrafo.Trip, reset:= reset, output=> Alarm_Matriz[18].03 );
	AlarmRecord[277](input:=RegT_Monitor_FusivelPonte.Alarme, reset:= reset, output=> Alarm_Matriz[18].04 );
	AlarmRecord[278](input:=RegT_Monitor_FusivelPonte.Trip, reset:= reset, output=> Alarm_Matriz[18].05 );
	AlarmRecord[279](input:=RegT_Monitor_41C.Alarme, reset:= reset, output=> Alarm_Matriz[18].06 );
	AlarmRecord[280](input:=RegT_Monitor_41C.Trip, reset:= reset, output=> Alarm_Matriz[18].07 );
	AlarmRecord[281](input:=RegT_Monitor_PreExcitacao.Alarme, reset:= reset, output=> Alarm_Matriz[18].08 );
	AlarmRecord[282](input:=RegT_Monitor_PreExcitacao.Trip, reset:= reset, output=> Alarm_Matriz[18].09 );
	AlarmRecord[283](input:=RegT_Monitor_Crowbar.Alarme, reset:= reset, output=> Alarm_Matriz[18].10 );
	AlarmRecord[284](input:=RegT_Monitor_Crowbar.Trip, reset:= reset, output=> Alarm_Matriz[18].11 );
	AlarmRecord[285](input:=RegT_Monitor_EscovaP.Alarme, reset:= reset, output=> Alarm_Matriz[18].12 );
	AlarmRecord[286](input:=RegT_Monitor_EscovaP.Trip, reset:= reset, output=> Alarm_Matriz[18].13 );
	AlarmRecord[287](input:=RegT_Monitor_EscovaN.Alarme, reset:= reset, output=> Alarm_Matriz[18].14 );
	AlarmRecord[288](input:=RegT_Monitor_EscovaN.Trip, reset:= reset, output=> Alarm_Matriz[18].15 );
	AlarmRecord[289](input:=RegT_Monitor_52L.Alarme, reset:= reset, output=> Alarm_Matriz[19].00 );
	AlarmRecord[290](input:=RegT_Monitor_52L.Trip, reset:= reset, output=> Alarm_Matriz[19].01 );
	(*AlarmRecord[291](input:=RegT.Reserva, reset:= reset, output=> Alarm_Matriz[19].02 );
	AlarmRecord[292](input:=RegT.Reserva, reset:= reset, output=> Alarm_Matriz[19].03 );
	AlarmRecord[293](input:=RegT.Reserva, reset:= reset, output=> Alarm_Matriz[19].04 );
	AlarmRecord[294](input:=RegT.Reserva, reset:= reset, output=> Alarm_Matriz[19].05 );
	AlarmRecord[295](input:=RegT.Reserva, reset:= reset, output=> Alarm_Matriz[19].06 );
	AlarmRecord[296](input:=RegT.Reserva, reset:= reset, output=> Alarm_Matriz[19].07 );
	AlarmRecord[297](input:=RegT.Reserva, reset:= reset, output=> Alarm_Matriz[19].08 );
	AlarmRecord[298](input:=RegT.Reserva, reset:= reset, output=> Alarm_Matriz[19].09 );
	AlarmRecord[299](input:=RegT.Reserva, reset:= reset, output=> Alarm_Matriz[19].10 );
	AlarmRecord[300](input:=RegT.Reserva, reset:= reset, output=> Alarm_Matriz[19].11 );
	AlarmRecord[301](input:=RegT.Reserva, reset:= reset, output=> Alarm_Matriz[19].12 );
	AlarmRecord[302](input:=RegT.Reserva, reset:= reset, output=> Alarm_Matriz[19].13 );
	AlarmRecord[303](input:=RegT.Reserva, reset:= reset, output=> Alarm_Matriz[19].14 );
	AlarmRecord[304](input:=RegT.Reserva, reset:= reset, output=> Alarm_Matriz[19].15 );*)

	(*j_Sincronismo*)
	AlarmRecord[305](input:=Sinc_Monitor.Alarme, reset:= reset, output=> Alarm_Matriz[20].00 );
	AlarmRecord[306](input:=Sinc_Monitor.Trip, reset:= reset, output=> Alarm_Matriz[20].01 );
	(*AlarmRecord[307](input:=Sinc.Reserva, reset:= reset, output=> Alarm_Matriz[20].02 );
	AlarmRecord[308](input:=Sinc.Reserva, reset:= reset, output=> Alarm_Matriz[20].03 );
	AlarmRecord[309](input:=Sinc.Reserva, reset:= reset, output=> Alarm_Matriz[20].04 );
	AlarmRecord[310](input:=Sinc.Reserva, reset:= reset, output=> Alarm_Matriz[20].05 );
	AlarmRecord[311](input:=Sinc.Reserva, reset:= reset, output=> Alarm_Matriz[20].06 );
	AlarmRecord[312](input:=Sinc.Reserva, reset:= reset, output=> Alarm_Matriz[20].07 );
	AlarmRecord[313](input:=Sinc.Reserva, reset:= reset, output=> Alarm_Matriz[20].08 );
	AlarmRecord[314](input:=Sinc.Reserva, reset:= reset, output=> Alarm_Matriz[20].09 );
	AlarmRecord[315](input:=Sinc.Reserva, reset:= reset, output=> Alarm_Matriz[20].10 );
	AlarmRecord[316](input:=Sinc.Reserva, reset:= reset, output=> Alarm_Matriz[20].11 );
	AlarmRecord[317](input:=Sinc.Reserva, reset:= reset, output=> Alarm_Matriz[20].12 );
	AlarmRecord[318](input:=Sinc.Reserva, reset:= reset, output=> Alarm_Matriz[20].13 );
	AlarmRecord[319](input:=Sinc.Reserva, reset:= reset, output=> Alarm_Matriz[20].14 );
	AlarmRecord[320](input:=Sinc.Reserva, reset:= reset, output=> Alarm_Matriz[20].15 );*)

	(*k_Reles_Bloqueio*)
	(*86M*)
	AlarmRecord[321](input:=ReleBloqueio_Monitor.Alarme, reset:= reset, output=> Alarm_Matriz[21].00 );
	AlarmRecord[322](input:= ReleBloqueio_Monitor.Trip, reset:= reset, output=> Alarm_Matriz[21].01 );
	AlarmRecord[323](input:= ReleBloqueio_Monitor_Acionamento.Alarme, reset:= reset, output=> Alarm_Matriz[21].02 );
	AlarmRecord[324](input:= ReleBloqueio_Monitor_Acionamento.Trip, reset:= reset, output=> Alarm_Matriz[21].03 );
	(*86E*)
	AlarmRecord[325](input:= ReleBloqueio_Monitor.Alarme, reset:= reset, output=> Alarm_Matriz[21].04 );
	AlarmRecord[326](input:= ReleBloqueio_Monitor.Trip, reset:= reset, output=> Alarm_Matriz[21].05 );
	AlarmRecord[327](input:= ReleBloqueio_Monitor_Acionamento.Alarme, reset:= reset, output=> Alarm_Matriz[21].06 );
	AlarmRecord[328](input:= ReleBloqueio_Monitor_Acionamento.Trip, reset:= reset, output=> Alarm_Matriz[21].07 );
	(*86H*)
	AlarmRecord[329](input:= ReleBloqueio_Monitor.Alarme, reset:= reset, output=> Alarm_Matriz[21].08 );
	AlarmRecord[330](input:= ReleBloqueio_Monitor.Trip, reset:= reset, output=> Alarm_Matriz[21].09 );
	AlarmRecord[331](input:= ReleBloqueio_Monitor_Acionamento.Alarme, reset:= reset, output=> Alarm_Matriz[21].10 );
	AlarmRecord[332](input:= ReleBloqueio_Monitor_Acionamento.Trip, reset:= reset, output=> Alarm_Matriz[21].11 );
	(*Reserva*)
	(*AlarmRecord[333](input:= ReleBloqueio.Reserva, reset:= reset, output=> Alarm_Matriz[21].12 );
	AlarmRecord[334](input:= ReleBloqueio.Reserva, reset:= reset, output=> Alarm_Matriz[21].13 );
	AlarmRecord[335](input:= ReleBloqueio.Reserva, reset:= reset, output=> Alarm_Matriz[21].14 );
	AlarmRecord[336](input:= ReleBloqueio.Reserva, reset:= reset, output=> Alarm_Matriz[21].15 );*)

	(*l_Analógicas*)

	(*m_Disjuntor_52G*)
	AlarmRecord[337](input:=Disj52G_Monitor_Abertura.Alarme, reset:= reset, output=> Alarm_Matriz[22].00 );
	AlarmRecord[338](input:= Disj52G_Monitor_Abertura.Trip, reset:= reset, output=> Alarm_Matriz[22].01 );
	AlarmRecord[339](input:= Disj52G_Monitor_Fechamento.Alarme, reset:= reset, output=> Alarm_Matriz[22].02 );
	AlarmRecord[340](input:= Disj52G_Monitor_Fechamento.Trip, reset:= reset, output=> Alarm_Matriz[22].03 );
	AlarmRecord[341](input:= Disj52G_Monitor_Motorizacao.Alarme, reset:= reset, output=> Alarm_Matriz[22].04 );
	AlarmRecord[342](input:= Disj52G_Monitor_Motorizacao.Trip, reset:= reset, output=> Alarm_Matriz[22].05 );
	AlarmRecord[343](input:= Disj52G_Monitor_Vauxiliar.Alarme, reset:= reset, output=> Alarm_Matriz[22].06 );
	AlarmRecord[344](input:= Disj52G_Monitor_Vauxiliar.Trip, reset:= reset, output=> Alarm_Matriz[22].07 );
	AlarmRecord[345](input:= Disj52G_Monitor_Grade.Alarme, reset:= reset, output=> Alarm_Matriz[22].08 );
	AlarmRecord[346](input:= Disj52G_Monitor_Grade.Trip, reset:= reset, output=> Alarm_Matriz[22].09 );
	AlarmRecord[347](input:= Disj52G_Monitor_Tampa.Alarme, reset:= reset, output=> Alarm_Matriz[22].10 );
	AlarmRecord[348](input:= Disj52G_Monitor_Tampa.Trip, reset:= reset, output=> Alarm_Matriz[22].11 );
	(*AlarmRecord[349](input:= Disj52G.Reserva, reset:= reset, output=> Alarm_Matriz[22].12 );
	AlarmRecord[350](input:= Disj52G.Reserva, reset:= reset, output=> Alarm_Matriz[22].13 );
	AlarmRecord[351](input:= Disj52G.Reserva, reset:= reset, output=> Alarm_Matriz[22].14 );
	AlarmRecord[352](input:= Disj52G.Reserva, reset:= reset, output=> Alarm_Matriz[22].15 );*)


	(*n_Disjuntores_Auxiliares*)
	AlarmRecord[353](input:=PCP_DisjQCCV.Falha_Aberto, reset:= reset, output=> Alarm_Matriz[23].00 );
	AlarmRecord[354](input:= PCP_DisjQCAG.Falha_Aberto, reset:= reset, output=> Alarm_Matriz[23].01 );
	AlarmRecord[355](input:= PCP_DisjQCAR.Falha_Aberto, reset:= reset, output=> Alarm_Matriz[23].02 );
	AlarmRecord[356](input:= CS_DisjQCC.Falha_Aberto, reset:= reset, output=> Alarm_Matriz[23].03 );
	AlarmRecord[357](input:= CS_DisjQCA01.Falha_Aberto, reset:= reset, output=> Alarm_Matriz[23].04 );
	AlarmRecord[358](input:= CS_DisjQCA02.Falha_Aberto, reset:= reset, output=> Alarm_Matriz[23].05 );
	(*AlarmRecord[359](input:= DisjAuxiliares.Reserva, reset:= reset, output=> Alarm_Matriz[23].06 );
	AlarmRecord[360](input:= DisjAuxiliares.Reserva, reset:= reset, output=> Alarm_Matriz[23].07 );
	AlarmRecord[361](input:= DisjAuxiliares.Reserva, reset:= reset, output=> Alarm_Matriz[23].08 );
	AlarmRecord[362](input:= DisjAuxiliares.Reserva, reset:= reset, output=> Alarm_Matriz[23].09 );
	AlarmRecord[363](input:= DisjAuxiliares.Reserva, reset:= reset, output=> Alarm_Matriz[23].10 );
	AlarmRecord[364](input:= DisjAuxiliares.Reserva, reset:= reset, output=> Alarm_Matriz[23].11 );
	AlarmRecord[365](input:= DisjAuxiliares.Reserva, reset:= reset, output=> Alarm_Matriz[23].12 );
	AlarmRecord[366](input:= DisjAuxiliares.Reserva, reset:= reset, output=> Alarm_Matriz[23].13 );
	AlarmRecord[367](input:= DisjAuxiliares.Reserva, reset:= reset, output=> Alarm_Matriz[23].14 );
	AlarmRecord[368](input:= DisjAuxiliares.Reserva, reset:= reset, output=> Alarm_Matriz[23].15 );*)

	(*o_Vibracao*)
	AlarmRecord[369](input:=Vibracao01_Monitor.Alarme, reset:= reset, output=> Alarm_Matriz[24].00);
	AlarmRecord[370](input:=Vibracao01_Monitor.Trip, reset:= reset, output=> Alarm_Matriz[24].01);
	AlarmRecord[371](input:=Vibracao02_Monitor.Alarme, reset:= reset, output=> Alarm_Matriz[24].02);
	AlarmRecord[372](input:=Vibracao02_Monitor.Trip, reset:= reset, output=> Alarm_Matriz[24].03);
	AlarmRecord[373](input:=Vibracao03_Monitor.Alarme, reset:= reset, output=> Alarm_Matriz[24].04);
	AlarmRecord[374](input:=Vibracao03_Monitor.Trip, reset:= reset, output=> Alarm_Matriz[24].05);
	AlarmRecord[375](input:=Vibracao04_Monitor.Alarme, reset:= reset, output=> Alarm_Matriz[24].06);
	AlarmRecord[376](input:=Vibracao04_Monitor.Trip, reset:= reset, output=> Alarm_Matriz[24].07);
	AlarmRecord[377](input:=Vibracao05_Monitor.Alarme, reset:= reset, output=> Alarm_Matriz[24].08);
	AlarmRecord[378](input:=Vibracao05_Monitor.Trip, reset:= reset, output=> Alarm_Matriz[24].09);
	(*AlarmRecord[379](input:=Vibracao.Reserva, reset:= reset, output=> Alarm_Matriz[24].10);
	AlarmRecord[380](input:=Vibracao.Reserva, reset:= reset, output=> Alarm_Matriz[24].11);
	AlarmRecord[381](input:=Vibracao.Reserva, reset:= reset, output=> Alarm_Matriz[24].12);
	AlarmRecord[382](input:=Vibracao.Reserva, reset:= reset, output=> Alarm_Matriz[24].13);
	AlarmRecord[383](input:=Vibracao.Reserva, reset:= reset, output=> Alarm_Matriz[24].14);
	AlarmRecord[384](input:=Vibracao.Reserva, reset:= reset, output=> Alarm_Matriz[24].15);*)

	(*p_Rele_Protecao*)
	AlarmRecord[385](input:= ReleProtecao.Falha_Trip, reset:= reset, output=> Alarm_Matriz[25].00 );
	AlarmRecord[386](input:= ReleProtecao.Falha_Watchdog, reset:= reset, output=> Alarm_Matriz[25].01 );
	AlarmRecord[387](input:= ReleProtecao.Falha_REG615_Prot_ON_01, reset:= reset, output=> Alarm_Matriz[25].02 );
	AlarmRecord[388](input:= ReleProtecao.Falha_REG615_Prot_ON_02, reset:= reset, output=> Alarm_Matriz[25].03 );
	AlarmRecord[389](input:= ReleProtecao.Falha_REG615_Prot_ON_03, reset:= reset, output=> Alarm_Matriz[25].04 );
	AlarmRecord[390](input:= ReleProtecao.Falha_REG615_Prot_ON_04, reset:= reset, output=> Alarm_Matriz[25].05 );
	AlarmRecord[391](input:= ReleProtecao.Falha_REG615_Prot_ON_05, reset:= reset, output=> Alarm_Matriz[25].06 );
	AlarmRecord[392](input:= ReleProtecao.Falha_REG615_Prot_ON_06, reset:= reset, output=> Alarm_Matriz[25].07 );
	AlarmRecord[393](input:= ReleProtecao.Falha_REG615_Prot_ON_07, reset:= reset, output=> Alarm_Matriz[25].08 );
	AlarmRecord[394](input:= ReleProtecao.Falha_REG615_Prot_ON_08, reset:= reset, output=> Alarm_Matriz[25].09 );
	AlarmRecord[395](input:= ReleProtecao.Falha_REG615_Prot_ON_09, reset:= reset, output=> Alarm_Matriz[25].10 );
	AlarmRecord[396](input:= ReleProtecao.Falha_REG615_Prot_ON_10, reset:= reset, output=> Alarm_Matriz[25].11 );
	AlarmRecord[397](input:= ReleProtecao.Falha_REG615_Prot_ON_11, reset:= reset, output=> Alarm_Matriz[25].12 );
	AlarmRecord[398](input:= ReleProtecao.Falha_REG615_Prot_ON_12, reset:= reset, output=> Alarm_Matriz[25].13 );
	AlarmRecord[399](input:= ReleProtecao.Falha_REG615_Prot_ON_13, reset:= reset, output=> Alarm_Matriz[25].14 );
	AlarmRecord[400](input:= ReleProtecao.Falha_REG615_Prot_ON_14, reset:= reset, output=> Alarm_Matriz[25].15 );
	AlarmRecord[401](input:= ReleProtecao.Falha_REG615_Prot_ON_15, reset:= reset, output=> Alarm_Matriz[26].00 );
	AlarmRecord[402](input:= ReleProtecao.Falha_REG615_Prot_ON_16, reset:= reset, output=> Alarm_Matriz[26].01 );
	(*AlarmRecord[403](input:= ReleProtecao.Falha_REG615_Prot_ON_17, reset:= reset, output=> Alarm_Matriz[26].02 );
	AlarmRecord[404](input:= ReleProtecao.Falha_REG615_Prot_ON_18, reset:= reset, output=> Alarm_Matriz[26].03 );
	AlarmRecord[405](input:= ReleProtecao.Falha_REG615_Prot_ON_19, reset:= reset, output=> Alarm_Matriz[26].04 );
	AlarmRecord[406](input:= ReleProtecao.Falha_REG615_Prot_ON_20, reset:= reset, output=> Alarm_Matriz[26].05 );
	AlarmRecord[407](input:= ReleProtecao.Falha_REG615_Prot_ON_21, reset:= reset, output=> Alarm_Matriz[26].06 );
	AlarmRecord[408](input:= ReleProtecao.Falha_REG615_Prot_ON_22, reset:= reset, output=> Alarm_Matriz[26].07 );
	AlarmRecord[409](input:= ReleProtecao.Falha_REG615_Prot_ON_23, reset:= reset, output=> Alarm_Matriz[26].08 );
	AlarmRecord[410](input:= ReleProtecao.Falha_REG615_Prot_ON_24, reset:= reset, output=> Alarm_Matriz[26].09 );
	AlarmRecord[411](input:= ReleProtecao.Falha_REG615_Prot_ON_25, reset:= reset, output=> Alarm_Matriz[26].10 );
	AlarmRecord[412](input:= ReleProtecao.Falha_REG615_Prot_ON_26, reset:= reset, output=> Alarm_Matriz[26].11 );
	AlarmRecord[413](input:= ReleProtecao.Falha_REG615_Prot_ON_27, reset:= reset, output=> Alarm_Matriz[26].12 );
	AlarmRecord[414](input:= ReleProtecao.Falha_REG615_Prot_ON_28, reset:= reset, output=> Alarm_Matriz[26].13 );
	AlarmRecord[415](input:= ReleProtecao.Falha_REG615_Prot_ON_29, reset:= reset, output=> Alarm_Matriz[26].14 );
	AlarmRecord[416](input:= ReleProtecao.Falha_REG615_Prot_ON_30, reset:= reset, output=> Alarm_Matriz[26].15 );
  	AlarmRecord[417](input:= ReleProtecao.Falha_REG615_Prot_ON_31, reset:= reset, output=> Alarm_Matriz[27].00, );
  	AlarmRecord[418](input:= ReleProtecao.Falha_REG615_Prot_ON_32, reset:= reset, output=> Alarm_Matriz[27].01 );*)

	(*q_Reset_Alarmes*)

	(*r_Totalizador_Potencia*)

	(*s_Temperaturas*)
	AlarmRecord[419](input:= Temperaturas01.Trip, reset:= reset, output=> Alarm_Matriz[28].00 );
	AlarmRecord[420](input:= Temperaturas01.Alarme, reset:= reset, output=> Alarm_Matriz[28].01 );
	AlarmRecord[421](input:= Temperaturas01.Sensor_Aberto, reset:= reset, output=> Alarm_Matriz[28].02 );
	AlarmRecord[422](input:= Temperaturas01.Sensor_EmCurto, reset:= reset, output=> Alarm_Matriz[28].03 );

	AlarmRecord[423](input:= Temperaturas02.Trip, reset:= reset, output=> Alarm_Matriz[28].04 );
	AlarmRecord[424](input:= Temperaturas02.Alarme, reset:= reset, output=> Alarm_Matriz[28].05 );
	AlarmRecord[425](input:= Temperaturas02.Sensor_Aberto, reset:= reset, output=> Alarm_Matriz[28].06 );
	AlarmRecord[426](input:= Temperaturas02.Sensor_EmCurto, reset:= reset, output=> Alarm_Matriz[28].07 );

	AlarmRecord[427](input:= Temperaturas03.Trip, reset:= reset, output=> Alarm_Matriz[28].08 );
	AlarmRecord[428](input:= Temperaturas03.Alarme, reset:= reset, output=> Alarm_Matriz[28].09 );
	AlarmRecord[429](input:= Temperaturas03.Sensor_Aberto, reset:= reset, output=> Alarm_Matriz[28].10 );
	AlarmRecord[430](input:= Temperaturas03.Sensor_EmCurto, reset:= reset, output=> Alarm_Matriz[28].11 );

	AlarmRecord[431](input:= Temperaturas04.Trip, reset:= reset, output=> Alarm_Matriz[28].12 );
	AlarmRecord[432](input:= Temperaturas04.Alarme, reset:= reset, output=> Alarm_Matriz[28].13 );
	AlarmRecord[433](input:= Temperaturas04.Sensor_Aberto, reset:= reset, output=> Alarm_Matriz[28].14 );
	AlarmRecord[434](input:= Temperaturas04.Sensor_EmCurto, reset:= reset, output=> Alarm_Matriz[28].15 );

	AlarmRecord[435](input:= Temperaturas05.Trip, reset:= reset, output=> Alarm_Matriz[29].00 );
	AlarmRecord[436](input:= Temperaturas05.Alarme, reset:= reset, output=> Alarm_Matriz[29].01 );
	AlarmRecord[437](input:= Temperaturas05.Sensor_Aberto, reset:= reset, output=> Alarm_Matriz[29].02 );
	AlarmRecord[438](input:= Temperaturas05.Sensor_EmCurto, reset:= reset, output=> Alarm_Matriz[29].03 );

	AlarmRecord[439](input:= Temperaturas06.Trip, reset:= reset, output=> Alarm_Matriz[29].04 );
	AlarmRecord[440](input:= Temperaturas06.Alarme, reset:= reset, output=> Alarm_Matriz[29].05 );
	AlarmRecord[441](input:= Temperaturas06.Sensor_Aberto, reset:= reset, output=> Alarm_Matriz[29].06 );
	AlarmRecord[442](input:= Temperaturas06.Sensor_EmCurto, reset:= reset, output=> Alarm_Matriz[29].07 );

	AlarmRecord[443](input:= Temperaturas07.Trip, reset:= reset, output=> Alarm_Matriz[29].08 );
	AlarmRecord[444](input:= Temperaturas07.Alarme, reset:= reset, output=> Alarm_Matriz[29].09 );
	AlarmRecord[445](input:= Temperaturas07.Sensor_Aberto, reset:= reset, output=> Alarm_Matriz[29].10 );
	AlarmRecord[446](input:= Temperaturas07.Sensor_EmCurto, reset:= reset, output=> Alarm_Matriz[29].11 );

	AlarmRecord[447](input:= Temperaturas08.Trip, reset:= reset, output=> Alarm_Matriz[29].12 );
	AlarmRecord[448](input:= Temperaturas08.Alarme, reset:= reset, output=> Alarm_Matriz[29].13 );
	AlarmRecord[449](input:= Temperaturas08.Sensor_Aberto, reset:= reset, output=> Alarm_Matriz[29].14 );
	AlarmRecord[450](input:= Temperaturas08.Sensor_EmCurto, reset:= reset, output=> Alarm_Matriz[29].15 );

	AlarmRecord[451](input:= Temperaturas09.Trip, reset:= reset, output=> Alarm_Matriz[30].00 );
	AlarmRecord[452](input:= Temperaturas09.Alarme, reset:= reset, output=> Alarm_Matriz[30].01 );
	AlarmRecord[453](input:= Temperaturas09.Sensor_Aberto, reset:= reset, output=> Alarm_Matriz[30].02 );
	AlarmRecord[454](input:= Temperaturas09.Sensor_EmCurto, reset:= reset, output=> Alarm_Matriz[30].03);

	AlarmRecord[455](input:= Temperaturas10.Trip, reset:= reset, output=> Alarm_Matriz[30].04 );
	AlarmRecord[456](input:= Temperaturas10.Alarme, reset:= reset, output=> Alarm_Matriz[30].05 );
	AlarmRecord[457](input:= Temperaturas10.Sensor_Aberto, reset:= reset, output=> Alarm_Matriz[30].06 );
	AlarmRecord[458](input:= Temperaturas10.Sensor_EmCurto, reset:= reset, output=> Alarm_Matriz[30].07 );

	AlarmRecord[459](input:= Temperaturas11.Trip, reset:= reset, output=> Alarm_Matriz[30].08 );
	AlarmRecord[460](input:= Temperaturas11.Alarme, reset:= reset, output=> Alarm_Matriz[30].09 );
	AlarmRecord[461](input:= Temperaturas11.Sensor_Aberto, reset:= reset, output=> Alarm_Matriz[30].10 );
	AlarmRecord[462](input:= Temperaturas11.Sensor_EmCurto, reset:= reset, output=> Alarm_Matriz[30].11 );

	AlarmRecord[463](input:= Temperaturas12.Trip, reset:= reset, output=> Alarm_Matriz[30].12 );
	AlarmRecord[464](input:= Temperaturas12.Alarme, reset:= reset, output=> Alarm_Matriz[30].13 );
	AlarmRecord[465](input:= Temperaturas12.Sensor_Aberto, reset:= reset, output=> Alarm_Matriz[30].14 );
	AlarmRecord[466](input:= Temperaturas12.Sensor_EmCurto, reset:= reset, output=> Alarm_Matriz[30].15 );

       (*t_Monitor_Barragem*)
	AlarmRecord[467](input:= Barragem_MonitorHH.Alarme, reset:= reset, output=> Alarm_Matriz[31].00 );
	AlarmRecord[468](input:= Barragem_MonitorHH.Trip, reset:= reset, output=> Alarm_Matriz[31].01 );
	AlarmRecord[469](input:= Barragem_MonitorH.Alarme, reset:= reset, output=> Alarm_Matriz[31].02 );
	AlarmRecord[470](input:= Barragem_MonitorH.Trip, reset:= reset, output=> Alarm_Matriz[31].03 );
	AlarmRecord[471](input:= Barragem_MonitorL.Alarme, reset:= reset, output=> Alarm_Matriz[31].04 );
	AlarmRecord[472](input:= Barragem_MonitorL.Trip, reset:= reset, output=> Alarm_Matriz[31].05 );
	AlarmRecord[473](input:= Barragem_MonitorLL.Alarme, reset:= reset, output=> Alarm_Matriz[31].06 );
	AlarmRecord[474](input:= Barragem_MonitorLL.Trip, reset:= reset, output=> Alarm_Matriz[31].07 );
	(*AlarmRecord[475](input:= MonitorNivel.Reserva, reset:= reset, output=> Alarm_Matriz[31].08 );
	AlarmRecord[476](input:= MonitorNivel.Reserva, reset:= reset, output=> Alarm_Matriz[31].09 );
	AlarmRecord[477](input:= MonitorNivel.Reserva, reset:= reset, output=> Alarm_Matriz[31].10 );
	AlarmRecord[478](input:= MonitorNivel.Reserva, reset:= reset, output=> Alarm_Matriz[31].11 );
	AlarmRecord[479](input:= MonitorNivel.Reserva, reset:= reset, output=> Alarm_Matriz[31].12 );
	AlarmRecord[480](input:= MonitorNivel.Reserva, reset:= reset, output=> Alarm_Matriz[31].13 );
	AlarmRecord[481](input:= MonitorNivel.Reserva, reset:= reset, output=> Alarm_Matriz[31].14 );
	AlarmRecord[482](input:= MonitorNivel.Reserva, reset:= reset, output=> Alarm_Matriz[31].15 );*)

	(*u_Horimetro*)

	(*z_Monitor_Comunicação*)
	AlarmRecord[483](input:= MonitorComunicacao.Falha_Comunicacao_GRTD2000, reset:= reset, output=> Alarm_Matriz[32].00 );
	AlarmRecord[484](input:= MonitorComunicacao.Falha_Comunicacao_REG615, reset:= reset, output=> Alarm_Matriz[32].01 );
	AlarmRecord[485](input:= MonitorComunicacao.Falha_Comunicacao_RIO600, reset:= reset, output=> Alarm_Matriz[32].02 );
	(*AlarmRecord[486](input:= MonitorComunicacao.Reserva, reset:= reset, output=> Alarm_Matriz[32].00 );
	AlarmRecord[487](input:= MonitorComunicacao.Reserva, reset:= reset, output=> Alarm_Matriz[32].01 );
	AlarmRecord[488](input:= MonitorComunicacao.Reserva, reset:= reset, output=> Alarm_Matriz[32].02 );
	AlarmRecord[489](input:= MonitorComunicacao.Reserva, reset:= reset, output=> Alarm_Matriz[32].00 );
	AlarmRecord[490](input:= MonitorComunicacao.Reserva, reset:= reset, output=> Alarm_Matriz[32].01 );
	AlarmRecord[491](input:= MonitorComunicacao.Reserva, reset:= reset, output=> Alarm_Matriz[32].02 );
	AlarmRecord[492](input:= MonitorComunicacao.Reserva, reset:= reset, output=> Alarm_Matriz[32].00 );
	AlarmRecord[493](input:= MonitorComunicacao.Reserva, reset:= reset, output=> Alarm_Matriz[32].01 );
	AlarmRecord[494](input:= MonitorComunicacao.Reserva, reset:= reset, output=> Alarm_Matriz[32].02 );
	AlarmRecord[495](input:= MonitorComunicacao.Reserva, reset:= reset, output=> Alarm_Matriz[32].00 );
	AlarmRecord[496](input:= MonitorComunicacao.Reserva, reset:= reset, output=> Alarm_Matriz[32].01 );
	AlarmRecord[497](input:= MonitorComunicacao.Reserva, reset:= reset, output=> Alarm_Matriz[32].02 );
	AlarmRecord[498](input:= MonitorComunicacao.Reserva, reset:= reset, output=> Alarm_Matriz[32].02 );*)


	(*Enge_AVS*)
	AlarmRecord[499](input:= GRTD_st_falha_load_par, reset:= reset, output=> Alarm_Matriz[33].00 );
	AlarmRecord[500](input:= GRTD_st_falha_store_par, reset:= reset, output=> Alarm_Matriz[33].01 );
	AlarmRecord[501](input:= GRTD_st_falha_erase_par, reset:= reset, output=> Alarm_Matriz[33].02 );
	AlarmRecord[502](input:= GRTD_st_al_irigb, reset:= reset, output=> Alarm_Matriz[33].03 );
	AlarmRecord[503](input:= GRTD_st_falha_com_dc, reset:= reset, output=> Alarm_Matriz[33].04 );
	AlarmRecord[504](input:= GRTD_st_falha_pt, reset:= reset, output=> Alarm_Matriz[33].05 );
	AlarmRecord[505](input:= GRTD_st_falha_sincr_dc, reset:= reset, output=> Alarm_Matriz[33].06 );
	AlarmRecord[506](input:= GRTD_st_falha_re_buf, reset:= reset, output=> Alarm_Matriz[33].07 );
	AlarmRecord[507](input:= GRTD_st_falha_load_log, reset:= reset, output=> Alarm_Matriz[33].08 );
	AlarmRecord[508](input:= GRTD_st_falha_store_log, reset:= reset, output=> Alarm_Matriz[33].09 );
	AlarmRecord[509](input:= GRTD_st_falha_erase_flash_log, reset:= reset, output=> Alarm_Matriz[33].10 );
	AlarmRecord[510](input:= GRTD_st_erro_logica, reset:= reset, output=> Alarm_Matriz[33].11 );
	AlarmRecord[511](input:= GRTD_st_mc_falha, reset:= reset, output=> Alarm_Matriz[33].12 );
	AlarmRecord[512](input:= GRTD_st_rt_al_esc_exc, reset:= reset, output=> Alarm_Matriz[33].13 );
	AlarmRecord[513](input:= GRTD_st_si_falha_sincr , reset:= reset, output=> Alarm_Matriz[33].14 );
	AlarmRecord[514](input:= GRTD_st_erro_sa1, reset:= reset, output=> Alarm_Matriz[33].15 );

	AlarmRecord[515](input:= GRTD_st_erro_sa2, reset:= reset, output=> Alarm_Matriz[34].00 );
	AlarmRecord[516](input:= GRTD_st_al_rea_varm, reset:= reset, output=> Alarm_Matriz[34].01 );
	AlarmRecord[517](input:= GRTD_st_reserva, reset:= reset, output=> Alarm_Matriz[34].02 );
	AlarmRecord[518](input:= GRTD_st_al_ge_ov1, reset:= reset, output=> Alarm_Matriz[34].03 );
	AlarmRecord[519](input:= GRTD_st_al_ge_un1, reset:= reset, output=> Alarm_Matriz[34].04 );
	AlarmRecord[520](input:= GRTD_st_al_ge_ov2 , reset:= reset, output=> Alarm_Matriz[34].05 );
	AlarmRecord[521](input:= GRTD_st_al_ge_un2, reset:= reset, output=> Alarm_Matriz[34].06 );
	AlarmRecord[522](input:= GRTD_st_al_ge_ov3, reset:= reset, output=> Alarm_Matriz[34].07 );
	AlarmRecord[523](input:= GRTD_st_al_ge_un3, reset:= reset, output=> Alarm_Matriz[34].08 );
	AlarmRecord[524](input:= GRTD_st_al_ge_ov4, reset:= reset, output=> Alarm_Matriz[34].09 );
	AlarmRecord[525](input:= GRTD_st_al_ge_un4, reset:= reset, output=> Alarm_Matriz[34].10 );
	AlarmRecord[526](input:= GRTD_st_al_ge_ov5, reset:= reset, output=> Alarm_Matriz[34].11 );
	AlarmRecord[527](input:= GRTD_st_al_ge_un5, reset:= reset, output=> Alarm_Matriz[34].12 );
	AlarmRecord[528](input:= GRTD_st_al_desb_iexc, reset:= reset, output=> Alarm_Matriz[34].13 );
	AlarmRecord[529](input:= GRTD_st_al_rea_vel, reset:= reset, output=> Alarm_Matriz[34].14 );
	AlarmRecord[530](input:= GRTD_st_al_rea_distr, reset:= reset, output=> Alarm_Matriz[34].15 );

	AlarmRecord[531](input:= GRTD_st_al_di_open, reset:= reset, output=> Alarm_Matriz[35].00 );
	AlarmRecord[532](input:= GRTD_st_al_di_close, reset:= reset, output=> Alarm_Matriz[35].01 );
	AlarmRecord[533](input:= GRTD_st_al_rea_rotor, reset:= reset, output=> Alarm_Matriz[35].02 );
	AlarmRecord[534](input:= GRTD_st_al_z_potp, reset:= reset, output=> Alarm_Matriz[35].03 );
	AlarmRecord[535](input:= GRTD_st_al_z_potq, reset:= reset, output=> Alarm_Matriz[35].04 );
	AlarmRecord[536](input:= GRTD_st_al_sinc_th, reset:= reset, output=> Alarm_Matriz[35].05 );
	AlarmRecord[537](input:= GRTD_st_al_desb_iarm, reset:= reset, output=> Alarm_Matriz[35].06 );
	(*AlarmRecord[538](input:= GRTD_Reserva, reset:= reset, output=> Alarm_Matriz[35].07 );
	AlarmRecord[539](input:= GRTD_Reserva, reset:= reset, output=> Alarm_Matriz[35].08 );
	AlarmRecord[540](input:= GRTD_Reserva, reset:= reset, output=> Alarm_Matriz[35].09 );
	AlarmRecord[541](input:= GRTD_Reserva, reset:= reset, output=> Alarm_Matriz[35].10 );
	AlarmRecord[542](input:= GRTD_Reserva, reset:= reset, output=> Alarm_Matriz[35].11 );
	AlarmRecord[543](input:= GRTD_Reserva, reset:= reset, output=> Alarm_Matriz[35].12 );
	AlarmRecord[544](input:= GRTD_Reserva, reset:= reset, output=> Alarm_Matriz[35].13 );
	AlarmRecord[545](input:= GRTD_Reserva, reset:= reset, output=> Alarm_Matriz[35].14 );
	AlarmRecord[546](input:= GRTD_Reserva, reset:= reset, output=> Alarm_Matriz[35].15 );*)
'''

TextoAddress = '''
(* 0x24289*)	Alarme_01					AT%MX750.0: BOOL;
(* 0x24290*)	Alarme_02					AT%MX750.1: BOOL;
(* 0x24291*)	Alarme_03					AT%MX750.2: BOOL;
(* 0x24292*)	Alarme_04					AT%MX750.3: BOOL;
(* 0x24293*)	Alarme_05					AT%MX750.4: BOOL;
(* 0x24294*)	Alarme_06					AT%MX750.5: BOOL;
(* 0x24295*)	Alarme_07					AT%MX750.6: BOOL;
(* 0x24296*)	Alarme_08					AT%MX750.7: BOOL;
(* 0x24297*)	Alarme_09					AT%MX750.8: BOOL;
(* 0x24298*)	Alarme_10					AT%MX750.9: BOOL;
(* 0x24299*)	Alarme_11						AT%MX750.10	: BOOL;
(* 0x24300*)	Alarme_12					AT%MX750.11	: BOOL;
(* 0x24301*)	Alarme_13					AT%MX750.12	: BOOL;
(* 0x24302*)	Alarme_14					AT%MX750.13	: BOOL;
(* 0x24303*)	Alarme_15					AT%MX750.14	: BOOL;
(* 0x24304*)	Alarme_16					AT%MX750.15	: BOOL;

(* 0x24305*)	Alarme_17					AT%MX751.0: BOOL;
(* 0x24306*)	Alarme_18					AT%MX751.1: BOOL;
(* 0x24307*)	Alarme_19					AT%MX751.2: BOOL;
(* 0x24308*)	Alarme_20					AT%MX751.3: BOOL;
(* 0x24309*)	Alarme_21					AT%MX751.4: BOOL;
(* 0x24310*)	Alarme_22					AT%MX751.5: BOOL;
(* 0x24311*)	Alarme_23					AT%MX751.6: BOOL;
(* 0x24312*)	Alarme_24					AT%MX751.7: BOOL;
(* 0x24313*)	Alarme_25					AT%MX751.8: BOOL;
(* 0x24314*)	Alarme_26					AT%MX751.9: BOOL;
(* 0x24315*)	Alarme_27					AT%MX751.10	: BOOL;
(* 0x24316*)	Alarme_28					AT%MX751.11	: BOOL;
(* 0x24317*)	Alarme_29					AT%MX751.12	: BOOL;
(* 0x24318*)	Alarme_30					AT%MX751.13	: BOOL;
(* 0x24319*)	Alarme_31					AT%MX751.14	: BOOL;
(* 0x24320*)	Alarme_32					AT%MX751.15	: BOOL;

(* 0x24321*)	Alarme_33					AT%MX752.0: BOOL;
(* 0x24322*)	Alarme_34					AT%MX752.1: BOOL;
(* 0x24323*)	Alarme_35					AT%MX752.2: BOOL;
(* 0x24324*)	Alarme_36					AT%MX752.3: BOOL;
(* 0x24325*)	Alarme_37					AT%MX752.4: BOOL;
(* 0x24326*)	Alarme_38					AT%MX752.5: BOOL;
(* 0x24327*)	Alarme_39					AT%MX752.6: BOOL;
(* 0x24328*)	Alarme_40					AT%MX752.7: BOOL;
(* 0x24329*)	Alarme_41					AT%MX752.8: BOOL;
(* 0x24330*)	Alarme_42					AT%MX752.9: BOOL;
(* 0x24331*)	Alarme_43					AT%MX752.10	: BOOL;
(* 0x24332*)	Alarme_44					AT%MX752.11	: BOOL;
(*0x24333*)	Alarme_45					AT%MX752.12	: BOOL;
(*0x24324*)	Alarme_46					AT%MX752.13	: BOOL;
(* 0x24335*)	Alarme_47					AT%MX752.14	: BOOL;
(* 0x24336*)	Alarme_48					AT%MX752.15	: BOOL;

(* 0x24337*)	Alarme_49					AT%MX753.0: BOOL;
(* 0x24338*)	Alarme_50					AT%MX753.1: BOOL;
(* 0x24339*)	Alarme_51					AT%MX753.2: BOOL;
(* 0x24340*)	Alarme_52					AT%MX753.3: BOOL;
(* 0x24341*)	Alarme_53					AT%MX753.4: BOOL;
(* 0x24342*)	Alarme_54					AT%MX753.5: BOOL;
(* 0x24343*)	Alarme_55					AT%MX753.6: BOOL;
(* 0x24344*)	Alarme_56					AT%MX753.7: BOOL;
(* 0x24345*)	Alarme_57					AT%MX753.8: BOOL;
(* 0x24346*)	Alarme_58					AT%MX753.9: BOOL;
(* 0x24347*)	Alarme_59					AT%MX753.10	: BOOL;
(* 0x24348*)	Alarme_60					AT%MX753.11	: BOOL;
(* 0x24349*)	Alarme_61					AT%MX753.12	: BOOL;
(* 0x24350*)	Alarme_62					AT%MX753.13	: BOOL;
(* 0x24351*)	Alarme_63					AT%MX753.14	: BOOL;
(* 0x24352*)	Alarme_64					AT%MX753.15	: BOOL;

(* 0x24353*)	Alarme_65					AT%MX754.0: BOOL;
(* 0x24354*)	Alarme_66					AT%MX754.1: BOOL;
(* 0x24355*)	Alarme_67					AT%MX754.2: BOOL;
(* 0x24356*)	Alarme_68					AT%MX754.3: BOOL;
(* 0x24357*)	Alarme_69					AT%MX754.4: BOOL;
(* 0x24358*)	Alarme_70					AT%MX754.5: BOOL;
(* 0x24359*)	Alarme_71					AT%MX754.6: BOOL;
(* 0x24360*)	Alarme_72					AT%MX754.7: BOOL;
(* 0x24361*)	Alarme_73					AT%MX754.8: BOOL;
(* 0x24362*)	Alarme_74					AT%MX754.9: BOOL;
(* 0x24363*)	Alarme_75					AT%MX754.10	: BOOL;
(* 0x24364*)	Alarme_76					AT%MX754.11	: BOOL;
(* 0x24365*)	Alarme_77					AT%MX754.12	: BOOL;
(* 0x24366*)	Alarme_78					AT%MX754.13	: BOOL;
(* 0x24367*)	Alarme_79					AT%MX754.14	: BOOL;
(* 0x24368*)	Alarme_80					AT%MX754.15	: BOOL;

(* 0x24369*)	Alarme_81					AT%MX755.0: BOOL;
(* 0x24370*)	Alarme_82					AT%MX755.1: BOOL;
(* 0x24371*)	Alarme_83					AT%MX755.2: BOOL;
(* 0x24372*)	Alarme_84					AT%MX755.3: BOOL;
(* 0x24373*)	Alarme_85					AT%MX755.4: BOOL;
(* 0x24374*)	Alarme_86					AT%MX755.5: BOOL;
(* 0x24375*)	Alarme_87					AT%MX755.6: BOOL;
(* 0x24376*)	Alarme_88					AT%MX755.7: BOOL;
(* 0x24377*)	Alarme_89					AT%MX755.8: BOOL;
(* 0x24378*)	Alarme_90					AT%MX755.9: BOOL;
(* 0x24379*)	Alarme_91					AT%MX755.10	: BOOL;
(* 0x24380*)	Alarme_92					AT%MX755.11	: BOOL;
(* 0x24381*)	Alarme_93					AT%MX755.12	: BOOL;
(* 0x24382*)	Alarme_94					AT%MX755.13	: BOOL;
(* 0x24383*)	Alarme_95					AT%MX755.14	: BOOL;
(* 0x24384*)	Alarme_96					AT%MX755.15	: BOOL;

(* 0x24385*)	Alarme_97					AT%MX756.0: BOOL;
(* 0x24386*)	Alarme_98					AT%MX756.1: BOOL;
(* 0x24387*)	Alarme_99					AT%MX756.2: BOOL;
(* 0x24388*)	Alarme_100					AT%MX756.3: BOOL;
(* 0x24389*)	Alarme_101					AT%MX756.4: BOOL;
(* 0x24390*)	Alarme_102					AT%MX756.5: BOOL;
(* 0x24391*)	Alarme_103					AT%MX756.6: BOOL;
(* 0x24392*)	Alarme_104					AT%MX756.7: BOOL;
(* 0x24393*)	Alarme_105					AT%MX756.8: BOOL;
(* 0x24394*)	Alarme_106					AT%MX756.9: BOOL;
(* 0x24395*)	Alarme_107					AT%MX756.10	: BOOL;
(* 0x24396*)	Alarme_108					AT%MX756.11	: BOOL;
(* 0x24397*)	Alarme_109					AT%MX756.12	: BOOL;
(* 0x24398*)	Alarme_110					AT%MX756.13	: BOOL;
(* 0x24399*)	Alarme_111					AT%MX756.14	: BOOL;
(* 0x24400*)	Alarme_112					AT%MX756.15	: BOOL;

(* 0x24401*)	Alarme_113					AT%MX757.0: BOOL;
(* 0x24402*)	Alarme_114					AT%MX757.1: BOOL;
(* 0x24403*)	Alarme_115					AT%MX757.2: BOOL;
(* 0x24404*)	Alarme_116					AT%MX757.3: BOOL;
(* 0x24405*)	Alarme_117					AT%MX757.4: BOOL;
(* 0x24406*)	Alarme_118					AT%MX757.5: BOOL;
(* 0x24407*)	Alarme_119					AT%MX757.6: BOOL;
(* 0x24408*)	Alarme_120					AT%MX757.7: BOOL;
(* 0x24409*)	Alarme_121					AT%MX757.8: BOOL;
(* 0x24410*)	Alarme_122					AT%MX757.9: BOOL;
(* 0x24411*)	Alarme_123					AT%MX757.10	: BOOL;
(* 0x24412*)	Alarme_124					AT%MX757.11	: BOOL;
(* 0x24413*)	Alarme_125					AT%MX757.12	: BOOL;
(* 0x24414*)	Alarme_126					AT%MX757.13	: BOOL;
(* 0x24415*)	Alarme_127					AT%MX757.14	: BOOL;
(* 0x24416*)	Alarme_128					AT%MX757.15	: BOOL;

(* 0x24417*)	Alarme_129					AT%MX758.0: BOOL;
(* 0x24418*)	Alarme_130					AT%MX758.1: BOOL;
(* 0x24419*)	Alarme_131					AT%MX758.2: BOOL;
(* 0x24420*)	Alarme_132					AT%MX758.3: BOOL;
(* 0x24421*)	Alarme_133					AT%MX758.4: BOOL;
(* 0x24422*)	Alarme_134					AT%MX758.5: BOOL;
(* 0x24423*)	Alarme_135					AT%MX758.6: BOOL;
(* 0x24424*)	Alarme_136					AT%MX758.7: BOOL;
(* 0x24425*)	Alarme_137					AT%MX758.8: BOOL;
(* 0x24426*)	Alarme_138					AT%MX758.9: BOOL;
(* 0x24427*)	Alarme_139					AT%MX758.10	: BOOL;
(* 0x24428*)	Alarme_140					AT%MX758.11	: BOOL;
(* 0x24429*)	Alarme_141					AT%MX758.12	: BOOL;
(* 0x24430*)	Alarme_142					AT%MX758.13	: BOOL;
(* 0x24431*)	Alarme_143					AT%MX758.14	: BOOL;
(* 0x24432*)	Alarme_144					AT%MX758.15	: BOOL;

(* 0x24433*)	Alarme_145					AT%MX759.0: BOOL;
(* 0x24434*)	Alarme_146					AT%MX759.1: BOOL;
(* 0x24435*)	Alarme_147					AT%MX759.2: BOOL;
(* 0x24436*)	Alarme_148					AT%MX759.3: BOOL;
(* 0x24437*)	Alarme_149					AT%MX759.4: BOOL;
(* 0x24438*)	Alarme_150					AT%MX759.5: BOOL;
(* 0x24439*)	Alarme_151					AT%MX759.6: BOOL;
(* 0x24440*)	Alarme_152					AT%MX759.7: BOOL;
(* 0x24441*)	Alarme_153					AT%MX759.8: BOOL;
(* 0x24442*)	Alarme_154					AT%MX759.9: BOOL;
(* 0x24443*)	Alarme_155					AT%MX759.10	: BOOL;
(* 0x24444*)	Alarme_156					AT%MX759.11	: BOOL;
(* 0x24445*)	Alarme_157					AT%MX759.12	: BOOL;
(* 0x24446*)	Alarme_158					AT%MX759.13	: BOOL;
(* 0x24447*)	Alarme_159					AT%MX759.14	: BOOL;
(* 0x24448*)	Alarme_160					AT%MX759.15	: BOOL;

(* 0x24449*)	Alarme_161					AT%MX760.0: BOOL;
(* 0x24450*)	Alarme_162					AT%MX760.1: BOOL;
(* 0x24451*)	Alarme_163					AT%MX760.2: BOOL;
(* 0x24452*)	Alarme_164					AT%MX760.3: BOOL;
(* 0x24453*)	Alarme_165					AT%MX760.4: BOOL;
(* 0x24454*)	Alarme_166					AT%MX760.5: BOOL;
(* 0x24455*)	Alarme_167					AT%MX760.6: BOOL;
(* 0x24456*)	Alarme_168					AT%MX760.7: BOOL;
(* 0x24457*)	Alarme_169					AT%MX760.8: BOOL;
(* 0x24458*)	Alarme_170					AT%MX760.9: BOOL;
(* 0x24459*)	Alarme_171					AT%MX760.10	: BOOL;
(* 0x24460*)	Alarme_172					AT%MX760.11	: BOOL;
(* 0x24461*)	Alarme_173					AT%MX760.12	: BOOL;
(* 0x24462*)	Alarme_174					AT%MX760.13	: BOOL;
(* 0x24463*)	Alarme_175					AT%MX760.14	: BOOL;
(* 0x24464*)	Alarme_176					AT%MX760.15	: BOOL;

(* 0x24465*)	Alarme_177					AT%MX761.0: BOOL;
(* 0x24466*)	Alarme_178					AT%MX761.1: BOOL;
(* 0x24467*)	Alarme_179					AT%MX761.2: BOOL;
(* 0x24468*)	Alarme_180					AT%MX761.3: BOOL;
(* 0x24469*)	Alarme_181					AT%MX761.4: BOOL;
(* 0x24470*)	Alarme_182					AT%MX761.5: BOOL;
(* 0x24471*)	Alarme_183					AT%MX761.6: BOOL;
(* 0x24472*)	Alarme_184					AT%MX761.7: BOOL;
(* 0x24473*)	Alarme_185					AT%MX761.8: BOOL;
(* 0x24474*)	Alarme_186					AT%MX761.9: BOOL;
(* 0x24475*)	Alarme_187					AT%MX761.10	: BOOL;
(* 0x24476*)	Alarme_188					AT%MX761.11	: BOOL;
(* 0x24477*)	Alarme_189					AT%MX761.12	: BOOL;
(* 0x24478*)	Alarme_190					AT%MX761.13	: BOOL;
(* 0x24479*)	Alarme_191					AT%MX761.14	: BOOL;
(* 0x24480*)	Alarme_192					AT%MX761.15	: BOOL;

(* 0x24481*)	Alarme_193					AT%MX762.0: BOOL;
(* 0x24482*)	Alarme_194					AT%MX762.1: BOOL;
(* 0x24483*)	Alarme_195					AT%MX762.2: BOOL;
(* 0x24484*)	Alarme_196					AT%MX762.3: BOOL;
(* 0x24485*)	Alarme_197					AT%MX762.4: BOOL;
(* 0x24486*)	Alarme_198					AT%MX762.5: BOOL;
(* 0x24487*)	Alarme_199					AT%MX762.6: BOOL;
(* 0x24488*)	Alarme_200					AT%MX762.7: BOOL;
(* 0x24489*)	Alarme_201					AT%MX762.8: BOOL;
(* 0x24490*)	Alarme_202					AT%MX762.9: BOOL;
(* 0x24491*)	Alarme_203					AT%MX762.10	: BOOL;
(* 0x24492*)	Alarme_204					AT%MX762.11	: BOOL;
(* 0x24493*)	Alarme_205					AT%MX762.12	: BOOL;
(* 0x24494*)	Alarme_206					AT%MX762.13	: BOOL;
(* 0x24495*)	Alarme_207					AT%MX762.14	: BOOL;
(* 0x24496*)	Alarme_208					AT%MX762.15	: BOOL;

(* 0x24497*)	Alarme_209					AT%MX763.0: BOOL;
(* 0x24498*)	Alarme_210					AT%MX763.1: BOOL;
(* 0x24499*)	Alarme_211					AT%MX763.2: BOOL;
(* 0x24500*)	Alarme_212					AT%MX763.3: BOOL;
(* 0x24501*)	Alarme_213					AT%MX763.4: BOOL;
(* 0x24502*)	Alarme_214					AT%MX763.5: BOOL;
(* 0x24503*)	Alarme_215					AT%MX763.6: BOOL;
(* 0x24504*)	Alarme_216					AT%MX763.7: BOOL;
(* 0x24505*)	Alarme_217					AT%MX763.8: BOOL;
(* 0x24506*)	Alarme_218					AT%MX763.9: BOOL;
(* 0x24507*)	Alarme_219					AT%MX763.10	: BOOL;
(* 0x24508*)	Alarme_220					AT%MX763.11	: BOOL;
(* 0x24509*)	Alarme_221					AT%MX763.12	: BOOL;
(* 0x24510*)	Alarme_222					AT%MX763.13	: BOOL;
(* 0x24511*)	Alarme_223					AT%MX763.14	: BOOL;
(* 0x24512*)	Alarme_224					AT%MX763.15	: BOOL;

(* 0x24513*)	Alarme_225					AT%MX764.0: BOOL;
(* 0x24514*)	Alarme_226					AT%MX764.1: BOOL;
(* 0x24515*)	Alarme_227					AT%MX764.2: BOOL;
(* 0x24516*)	Alarme_228					AT%MX764.3: BOOL;
(* 0x24517*)	Alarme_229					AT%MX764.4: BOOL;
(* 0x24518*)	Alarme_230					AT%MX764.5: BOOL;
(* 0x24519*)	Alarme_231					AT%MX764.6: BOOL;
(* 0x24520*)	Alarme_232					AT%MX764.7: BOOL;
(* 0x24521*)	Alarme_233					AT%MX764.8: BOOL;
(* 0x24522*)	Alarme_234					AT%MX764.9: BOOL;
(* 0x24523*)	Alarme_235					AT%MX764.10	: BOOL;
(* 0x24524*)	Alarme_236					AT%MX764.11	: BOOL;
(* 0x24525*)	Alarme_237					AT%MX764.12	: BOOL;
(* 0x24526*)	Alarme_238					AT%MX764.13	: BOOL;
(* 0x24527*)	Alarme_239					AT%MX764.14	: BOOL;
(* 0x24528*)	Alarme_240					AT%MX764.15	: BOOL;

(* 0x24529*)	Alarme_241					AT%MX765.0: BOOL;
(* 0x24530*)	Alarme_242					AT%MX765.1: BOOL;
(* 0x24531*)	Alarme_243					AT%MX765.2: BOOL;
(* 0x24532*)	Alarme_244					AT%MX765.3: BOOL;
(* 0x24533*)	Alarme_245					AT%MX765.4: BOOL;
(* 0x24534*)	Alarme_246					AT%MX765.5: BOOL;
(* 0x24535*)	Alarme_247					AT%MX765.6: BOOL;
(* 0x24536*)	Alarme_248					AT%MX765.7: BOOL;
(* 0x24537*)	Alarme_249					AT%MX765.8: BOOL;
(* 0x24538*)	Alarme_250					AT%MX765.9: BOOL;
(* 0x24539*)	Alarme_251					AT%MX765.10	: BOOL;
(* 0x24540*)	Alarme_252					AT%MX765.11	: BOOL;
(* 0x24541*)	Alarme_253					AT%MX765.12	: BOOL;
(* 0x24542*)	Alarme_254					AT%MX765.13	: BOOL;
(* 0x24543*)	Alarme_255					AT%MX765.14	: BOOL;
(* 0x24544*)	Alarme_256					AT%MX765.15	: BOOL;

(* 0x24545*)	Alarme_257					AT%MX766.0: BOOL;
(* 0x24546*)	Alarme_258					AT%MX766.1: BOOL;
(* 0x24547*)	Alarme_259					AT%MX766.2: BOOL;
(* 0x24548*)	Alarme_260					AT%MX766.3: BOOL;
(* 0x24549*)	Alarme_261					AT%MX766.4: BOOL;
(* 0x24550*)	Alarme_262					AT%MX766.5: BOOL;
(* 0x24551*)	Alarme_263					AT%MX766.6: BOOL;
(* 0x24552*)	Alarme_264					AT%MX766.7: BOOL;
(* 0x24553*)	Alarme_265					AT%MX766.8: BOOL;
(* 0x24554*)	Alarme_266					AT%MX766.9: BOOL;
(* 0x24555*)	Alarme_267					AT%MX766.10	: BOOL;
(* 0x24556*)	Alarme_268					AT%MX766.11	: BOOL;
(* 0x24557*)	Alarme_269					AT%MX766.12	: BOOL;
(* 0x24558*)	Alarme_270					AT%MX766.13	: BOOL;
(* 0x24559*)	Alarme_271					AT%MX766.14	: BOOL;
(* 0x24560*)	Alarme_272					AT%MX766.15	: BOOL;

(* 0x24561*)	Alarme_273					AT%MX767.0: BOOL;
(* 0x24562*)	Alarme_274					AT%MX767.1: BOOL;
(* 0x24563*)	Alarme_275					AT%MX767.2: BOOL;
(* 0x24564*)	Alarme_276					AT%MX767.3: BOOL;
(* 0x24565*)	Alarme_277					AT%MX767.4: BOOL;
(* 0x24566*)	Alarme_278					AT%MX767.5: BOOL;
(* 0x24567*)	Alarme_279					AT%MX767.6: BOOL;
(* 0x24568*)	Alarme_280					AT%MX767.7: BOOL;
(* 0x24569*)	Alarme_281					AT%MX767.8: BOOL;
(* 0x24570*)	Alarme_282					AT%MX767.9: BOOL;
(* 0x24571*)	Alarme_283					AT%MX767.10	: BOOL;
(* 0x24572*)	Alarme_284					AT%MX767.11	: BOOL;
(* 0x24573*)	Alarme_285					AT%MX767.12	: BOOL;
(* 0x24574*)	Alarme_286					AT%MX767.13	: BOOL;
(* 0x24575*)	Alarme_287					AT%MX767.14	: BOOL;
(* 0x24576*)	Alarme_288					AT%MX767.15	: BOOL;

(* 0x24577*)	Alarme_289					AT%MX768.0: BOOL;
(* 0x24578*)	Alarme_290					AT%MX768.1: BOOL;
(* 0x24579*)	Alarme_291					AT%MX768.2: BOOL;
(* 0x24580*)	Alarme_292					AT%MX768.3: BOOL;
(* 0x24581*)	Alarme_293					AT%MX768.4: BOOL;
(* 0x24582*)	Alarme_294					AT%MX768.5: BOOL;
(* 0x24583*)	Alarme_295					AT%MX768.6: BOOL;
(* 0x24584*)	Alarme_296					AT%MX768.7: BOOL;
(* 0x24585*)	Alarme_297					AT%MX768.8: BOOL;
(* 0x24586*)	Alarme_298					AT%MX768.9: BOOL;
(* 0x24587*)	Alarme_299					AT%MX768.10	: BOOL;
(* 0x24588*)	Alarme_300					AT%MX768.11	: BOOL;
(* 0x24589*)	Alarme_301					AT%MX768.12	: BOOL;
(* 0x24590*)	Alarme_302					AT%MX768.13	: BOOL;
(* 0x24591*)	Alarme_303					AT%MX768.14	: BOOL;
(* 0x24592*)	Alarme_304					AT%MX768.15	: BOOL;

(* 0x24593*)	Alarme_305					AT%MX769.0: BOOL;
(* 0x24594*)	Alarme_306					AT%MX769.1: BOOL;
(* 0x24595*)	Alarme_307					AT%MX769.2: BOOL;
(* 0x24596*)	Alarme_308					AT%MX769.3: BOOL;
(* 0x24597*)	Alarme_309					AT%MX769.4: BOOL;
(* 0x24598*)	Alarme_310					AT%MX769.5: BOOL;
(* 0x24599*)	Alarme_311					AT%MX769.6: BOOL;
(* 0x24600*)	Alarme_312					AT%MX769.7: BOOL;
(* 0x24601*)	Alarme_313					AT%MX769.8: BOOL;
(* 0x24602*)	Alarme_314					AT%MX769.9: BOOL;
(* 0x24603*)	Alarme_315					AT%MX769.10	: BOOL;
(* 0x24604*)	Alarme_316					AT%MX769.11	: BOOL;
(* 0x24605*)	Alarme_317					AT%MX769.12	: BOOL;
(* 0x24606*)	Alarme_318					AT%MX769.13	: BOOL;
(* 0x24607*)	Alarme_319					AT%MX769.14	: BOOL;
(* 0x24608*)	Alarme_320					AT%MX769.15	: BOOL;

(* 0x24609*)	Alarme_321					AT%MX770.0: BOOL;
(* 0x24610*)	Alarme_322					AT%MX770.1: BOOL;
(* 0x24611*)	Alarme_323					AT%MX770.2: BOOL;
(* 0x24612*)	Alarme_324					AT%MX770.3: BOOL;
(* 0x24613*)	Alarme_325					AT%MX770.4: BOOL;
(* 0x24614*)	Alarme_326					AT%MX770.5: BOOL;
(* 0x24615*)	Alarme_327					AT%MX770.6: BOOL;
(* 0x24616*)	Alarme_328					AT%MX770.7: BOOL;
(* 0x24617*)	Alarme_329					AT%MX770.8: BOOL;
(* 0x24618*)	Alarme_330					AT%MX770.9: BOOL;
(* 0x24619*)	Alarme_331					AT%MX770.10	: BOOL;
(* 0x24620*)	Alarme_332					AT%MX770.11	: BOOL;
(* 0x24621*)	Alarme_333					AT%MX770.12	: BOOL;
(* 0x24622*)	Alarme_334					AT%MX770.13	: BOOL;
(* 0x24623*)	Alarme_335					AT%MX770.14	: BOOL;
(* 0x24624*)	Alarme_336					AT%MX770.15	: BOOL;

(* 0x24625*)	Alarme_337					AT%MX771.0: BOOL;
(* 0x24626*)	Alarme_338					AT%MX771.1: BOOL;
(* 0x24627*)	Alarme_339					AT%MX771.2: BOOL;
(* 0x24628*)	Alarme_340					AT%MX771.3: BOOL;
(* 0x24629*)	Alarme_341					AT%MX771.4: BOOL;
(* 0x24630*)	Alarme_342					AT%MX771.5: BOOL;
(* 0x24631*)	Alarme_343					AT%MX771.6: BOOL;
(* 0x24632*)	Alarme_344					AT%MX771.7: BOOL;
(* 0x24633*)	Alarme_345					AT%MX771.8: BOOL;
(* 0x24634*)	Alarme_346					AT%MX771.9: BOOL;
(* 0x24635*)	Alarme_347					AT%MX771.10	: BOOL;
(* 0x24636*)	Alarme_348					AT%MX771.11	: BOOL;
(* 0x24637*)	Alarme_349					AT%MX771.12	: BOOL;
(* 0x24638*)	Alarme_350					AT%MX771.13	: BOOL;
(* 0x24639*)	Alarme_351					AT%MX771.14	: BOOL;
(* 0x24640*)	Alarme_352					AT%MX771.15	: BOOL;

(* 0x24641*)	Alarme_353					AT%MX772.0: BOOL;
(* 0x24642*)	Alarme_354					AT%MX772.1: BOOL;
(* 0x24643*)	Alarme_355					AT%MX772.2: BOOL;
(* 0x24644*)	Alarme_356					AT%MX772.3: BOOL;
(* 0x24645*)	Alarme_357					AT%MX772.4: BOOL;
(* 0x24646*)	Alarme_358					AT%MX772.5: BOOL;
(* 0x24647*)	Alarme_359					AT%MX772.6: BOOL;
(* 0x24648*)	Alarme_360					AT%MX772.7: BOOL;
(* 0x24649*)	Alarme_361					AT%MX772.8: BOOL;
(* 0x24650*)	Alarme_362					AT%MX772.9: BOOL;
(* 0x24651*)	Alarme_363					AT%MX772.10	: BOOL;
(* 0x24652*)	Alarme_364					AT%MX772.11	: BOOL;
(* 0x24653*)	Alarme_365					AT%MX772.12	: BOOL;
(* 0x24654*)	Alarme_366					AT%MX772.13	: BOOL;
(* 0x24655*)	Alarme_367					AT%MX772.14	: BOOL;
(* 0x24656*)	Alarme_368					AT%MX772.15	: BOOL;

(* 0x24657*)	Alarme_369					AT%MX773.0: BOOL;
(* 0x24658*)	Alarme_370					AT%MX773.1: BOOL;
(* 0x24659*)	Alarme_371					AT%MX773.2: BOOL;
(* 0x24660*)	Alarme_372					AT%MX773.3: BOOL;
(* 0x24661*)	Alarme_373					AT%MX773.4: BOOL;
(* 0x24662*)	Alarme_374					AT%MX773.5: BOOL;
(* 0x24663*)	Alarme_375					AT%MX773.6: BOOL;
(* 0x24664*)	Alarme_376					AT%MX773.7: BOOL;
(* 0x24665*)	Alarme_377					AT%MX773.8: BOOL;
(* 0x24666*)	Alarme_378					AT%MX773.9: BOOL;
(* 0x24667*)	Alarme_379					AT%MX773.10	: BOOL;
(* 0x24668*)	Alarme_380					AT%MX773.11	: BOOL;
(* 0x24669*)	Alarme_381					AT%MX773.12	: BOOL;
(* 0x24670*)	Alarme_382					AT%MX773.13	: BOOL;
(* 0x24671*)	Alarme_383					AT%MX773.14	: BOOL;
(* 0x24672*)	Alarme_384					AT%MX773.15	: BOOL;

(* 0x24673*)	Alarme_385					AT%MX774.0: BOOL;
(* 0x24674*)	Alarme_386					AT%MX774.1: BOOL;
(* 0x24675*)	Alarme_387					AT%MX774.2: BOOL;
(* 0x24676*)	Alarme_388					AT%MX774.3: BOOL;
(* 0x24677*)	Alarme_389					AT%MX774.4: BOOL;
(* 0x24678*)	Alarme_390					AT%MX774.5: BOOL;
(* 0x24679*)	Alarme_391					AT%MX774.6: BOOL;
(* 0x24680*)	Alarme_392					AT%MX774.7: BOOL;
(* 0x24681*)	Alarme_393					AT%MX774.8: BOOL;
(* 0x24682*)	Alarme_394					AT%MX774.9: BOOL;
(* 0x24683*)	Alarme_395					AT%MX774.10	: BOOL;
(* 0x24684*)	Alarme_396					AT%MX774.11	: BOOL;
(* 0x24685*)	Alarme_397					AT%MX774.12	: BOOL;
(* 0x24686*)	Alarme_398					AT%MX774.13	: BOOL;
(* 0x24687*)	Alarme_399					AT%MX774.14	: BOOL;
(* 0x24688*)	Alarme_400					AT%MX774.15	: BOOL;

(* 0x24689*)	Alarme_401					AT%MX775.0: BOOL;
(* 0x24690*)	Alarme_402					AT%MX775.1: BOOL;
(* 0x24691*)	Alarme_403					AT%MX775.2: BOOL;
(* 0x24692*)	Alarme_404					AT%MX775.3: BOOL;
(* 0x24693*)	Alarme_405					AT%MX775.4: BOOL;
(* 0x24694*)	Alarme_406					AT%MX775.5: BOOL;
(* 0x24695*)	Alarme_407					AT%MX775.6: BOOL;
(* 0x24696*)	Alarme_408					AT%MX775.7: BOOL;
(* 0x24697*)	Alarme_409					AT%MX775.8: BOOL;
(* 0x24698*)	Alarme_410					AT%MX775.9: BOOL;
(* 0x24699*)	Alarme_411					AT%MX775.10	: BOOL;
(* 0x24700*)	Alarme_412					AT%MX775.11	: BOOL;
(* 0x24701*)	Alarme_413					AT%MX775.12	: BOOL;
(* 0x24702*)	Alarme_414					AT%MX775.13	: BOOL;
(* 0x24703*)	Alarme_415					AT%MX775.14	: BOOL;
(* 0x24704*)	Alarme_416					AT%MX775.15	: BOOL;

(* 0x24705*)	Alarme_417					AT%MX776.0: BOOL;
(* 0x24706*)	Alarme_418					AT%MX776.1: BOOL;
(* 0x24707*)	Alarme_419					AT%MX776.2: BOOL;
(* 0x24708*)	Alarme_420					AT%MX776.3: BOOL;
(* 0x24709*)	Alarme_421					AT%MX776.4: BOOL;
(* 0x24710*)	Alarme_422					AT%MX776.5: BOOL;
(* 0x24711*)	Alarme_423					AT%MX776.6: BOOL;
(* 0x24712*)	Alarme_424					AT%MX776.7: BOOL;
(* 0x24713*)	Alarme_425					AT%MX776.8: BOOL;
(* 0x24714*)	Alarme_426					AT%MX776.9: BOOL;
(* 0x24715*)	Alarme_427					AT%MX776.10	: BOOL;
(* 0x24716*)	Alarme_428					AT%MX776.11	: BOOL;
(* 0x24717*)	Alarme_429					AT%MX776.12	: BOOL;
(* 0x24718*)	Alarme_430					AT%MX776.13	: BOOL;
(* 0x24719*)	Alarme_431					AT%MX776.14	: BOOL;
(* 0x24720*)	Alarme_432					AT%MX776.15	: BOOL;

(* 0x24721*)	Alarme_433					AT%MX777.0: BOOL;
(* 0x24722*)	Alarme_434					AT%MX777.1: BOOL;
(* 0x24723*)	Alarme_435					AT%MX777.2: BOOL;
(* 0x24724*)	Alarme_436					AT%MX777.3: BOOL;
(* 0x24725*)	Alarme_437					AT%MX777.4: BOOL;
(* 0x24726*)	Alarme_438					AT%MX777.5: BOOL;
(* 0x24727*)	Alarme_439					AT%MX777.6: BOOL;
(* 0x24728*)	Alarme_440					AT%MX777.7: BOOL;
(* 0x24729*)	Alarme_441					AT%MX777.8: BOOL;
(* 0x24730*)	Alarme_442					AT%MX777.9: BOOL;
(* 0x24731*)	Alarme_443					AT%MX777.10	: BOOL;
(* 0x24732*)	Alarme_444					AT%MX777.11	: BOOL;
(* 0x24733*)	Alarme_445					AT%MX777.12	: BOOL;
(* 0x24734*)	Alarme_446					AT%MX777.13	: BOOL;
(* 0x24735*)	Alarme_447					AT%MX777.14	: BOOL;
(* 0x24736*)	Alarme_448					AT%MX777.15	: BOOL;

(* 0x24737*)	Alarme_449					AT%MX778.0: BOOL;
(* 0x24738*)	Alarme_450					AT%MX778.1: BOOL;
(* 0x24739*)	Alarme_451					AT%MX778.2: BOOL;
(* 0x24740*)	Alarme_452					AT%MX778.3: BOOL;
(* 0x24741*)	Alarme_453					AT%MX778.4: BOOL;
(* 0x24742*)	Alarme_454					AT%MX778.5: BOOL;
(* 0x24743*)	Alarme_455					AT%MX778.6: BOOL;
(* 0x24744*)	Alarme_456					AT%MX778.7: BOOL;
(* 0x24745*)	Alarme_457					AT%MX778.8: BOOL;
(* 0x24746*)	Alarme_458					AT%MX778.9: BOOL;
(* 0x24747*)	Alarme_459					AT%MX778.10	: BOOL;
(* 0x24748*)	Alarme_460					AT%MX778.11	: BOOL;
(* 0x24749*)	Alarme_461					AT%MX778.12	: BOOL;
(* 0x24750*)	Alarme_462					AT%MX778.13	: BOOL;
(* 0x24751*)	Alarme_463					AT%MX778.14	: BOOL;
(* 0x24752*)	Alarme_464					AT%MX778.15	: BOOL;

(* 0x24753*)	Alarme_465					AT%MX779.0: BOOL;
(* 0x24754*)	Alarme_466					AT%MX779.1: BOOL;
(* 0x24755*)	Alarme_467					AT%MX779.2: BOOL;
(* 0x24756*)	Alarme_468					AT%MX779.3: BOOL;
(* 0x24757*)	Alarme_469					AT%MX779.4: BOOL;
(* 0x24758*)	Alarme_470					AT%MX779.5: BOOL;
(* 0x24759*)	Alarme_471					AT%MX779.6: BOOL;
(* 0x24760*)	Alarme_472					AT%MX779.7: BOOL;
(* 0x24761*)	Alarme_473					AT%MX779.8: BOOL;
(* 0x24762*)	Alarme_474					AT%MX779.9: BOOL;
(* 0x24763*)	Alarme_475					AT%MX779.10	: BOOL;
(* 0x24764*)	Alarme_476					AT%MX779.11	: BOOL;
(* 0x24765*)	Alarme_477					AT%MX779.12	: BOOL;
(* 0x24766*)	Alarme_478					AT%MX779.13	: BOOL;
(* 0x24767*)	Alarme_479					AT%MX779.14	: BOOL;
(* 0x24768*)	Alarme_480					AT%MX779.15	: BOOL;

(* 0x24769*)	Alarme_481					AT%MX780.0: BOOL;
(* 0x24770*)	Alarme_482					AT%MX780.1: BOOL;
(* 0x24771*)	Alarme_483					AT%MX780.2: BOOL;
(* 0x24772*)	Alarme_484					AT%MX780.3: BOOL;
(* 0x24773*)	Alarme_485					AT%MX780.4: BOOL;
(* 0x24774*)	Alarme_486					AT%MX780.5: BOOL;
(* 0x24775*)	Alarme_487					AT%MX780.6: BOOL;
(* 0x24776*)	Alarme_488					AT%MX780.7: BOOL;
(* 0x24777*)	Alarme_489					AT%MX780.8: BOOL;
(* 0x24778*)	Alarme_490					AT%MX780.9: BOOL;
(* 0x24779*)	Alarme_491					AT%MX780.10	: BOOL;
(* 0x24780*)	Alarme_492					AT%MX780.11	: BOOL;
(* 0x24781*)	Alarme_493					AT%MX780.12	: BOOL;
(* 0x24782*)	Alarme_494					AT%MX780.13	: BOOL;
(* 0x24783*)	Alarme_495					AT%MX780.14	: BOOL;
(* 0x24784*)	Alarme_496					AT%MX780.15	: BOOL;

(* 0x24785*)	Alarme_497					AT%MX781.0: BOOL;
(* 0x24786*)	Alarme_498					AT%MX781.1: BOOL;
(* 0x24787*)	Alarme_499					AT%MX781.2: BOOL;
(* 0x24788*)	Alarme_500					AT%MX781.3: BOOL;
(* 0x24789*)	Alarme_501					AT%MX781.4: BOOL;
(* 0x24790*)	Alarme_502					AT%MX781.5: BOOL;
(* 0x24791*)	Alarme_503					AT%MX781.6: BOOL;
(* 0x24792*)	Alarme_504					AT%MX781.7: BOOL;
(* 0x24793*)	Alarme_505					AT%MX781.8: BOOL;
(* 0x24794*)	Alarme_506					AT%MX781.9: BOOL;
(* 0x24795*)	Alarme_507					AT%MX781.10	: BOOL;
(* 0x24796*)	Alarme_508					AT%MX781.11	: BOOL;
(* 0x24797*)	Alarme_509					AT%MX781.12	: BOOL;
(* 0x24798*)	Alarme_510					AT%MX781.13	: BOOL;
(* 0x24799*)	Alarme_511					AT%MX781.14	: BOOL;
(* 0x24800*)	Alarme_512					AT%MX781.15	: BOOL;

(* 0x24801*)	Alarme_513					AT%MX782.0: BOOL;
(* 0x24802*)	Alarme_514					AT%MX782.1: BOOL;
(* 0x24803*)	Alarme_515					AT%MX782.2: BOOL;
(* 0x24804*)	Alarme_516					AT%MX782.3: BOOL;
(* 0x24805*)	Alarme_517					AT%MX782.4: BOOL;
(* 0x24806*)	Alarme_518					AT%MX782.5: BOOL;
(* 0x24807*)	Alarme_519					AT%MX782.6: BOOL;
(* 0x24808*)	Alarme_520					AT%MX782.7: BOOL;
(* 0x24809*)	Alarme_521					AT%MX782.8: BOOL;
(* 0x24810*)	Alarme_522					AT%MX782.9: BOOL;
(* 0x24811*)	Alarme_523					AT%MX782.10	: BOOL;
(* 0x24812*)	Alarme_524					AT%MX782.11	: BOOL;
(* 0x24813*)	Alarme_525					AT%MX782.12	: BOOL;
(* 0x24814*)	Alarme_526					AT%MX782.13	: BOOL;
(* 0x24815*)	Alarme_527					AT%MX782.14	: BOOL;
(* 0x24816*)	Alarme_528					AT%MX782.15	: BOOL;

(* 0x24817*)	Alarme_529					AT%MX783.0: BOOL;
(* 0x24818*)	Alarme_530					AT%MX783.1: BOOL;
(* 0x24819*)	Alarme_531					AT%MX783.2: BOOL;
(* 0x24820*)	Alarme_532					AT%MX783.3: BOOL;
(* 0x24821*)	Alarme_533					AT%MX783.4: BOOL;
(* 0x24822*)	Alarme_534					AT%MX783.5: BOOL;
(* 0x24823*)	Alarme_535					AT%MX783.6: BOOL;
(* 0x24824*)	Alarme_536					AT%MX783.7: BOOL;
(* 0x24825*)	Alarme_537					AT%MX783.8: BOOL;
(* 0x24826*)	Alarme_538					AT%MX783.9: BOOL;
(* 0x24827*)	Alarme_539					AT%MX783.10	: BOOL;
(* 0x24828*)	Alarme_540					AT%MX783.11	: BOOL;
(* 0x24829*)	Alarme_541					AT%MX783.12	: BOOL;
(* 0x24830*)	Alarme_542					AT%MX783.13	: BOOL;
(* 0x24831*)	Alarme_543					AT%MX783.14	: BOOL;
(* 0x24832*)	Alarme_544					AT%MX783.15	: BOOL;
'''