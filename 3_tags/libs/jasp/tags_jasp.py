comandos = '''
		(*Painel de Controle*)
		(*01x12289*) Emergencia_Local						AT%MX0.0: BOOL;
		(*01x12290*) Emergencia_SuperSEP				AT%MX0.1: BOOL;
		(*01x12291*) Ctrl_Modo_Manual_Habilitar			AT%MX0.2: BOOL;
		(*01x12292*) Ctrl_Modo_Manual_Desabilitar		AT%MX0.3: BOOL;
		(*01x12293*) Ctrl_Modo_Automatico_Habilitar		AT%MX0.4: BOOL;
		(*01x12294*) Ctrl_Modo_Automatico_Desabilitar	AT%MX0.5: BOOL;
		(*01x12295*) Reserva_12995						AT%MX0.6: BOOL;
		(*01x12296*) Reserva_12996						AT%MX0.7: BOOL;
		(*01x12297*) Reserva_12997						AT%MX0.8: BOOL;
		(*01x12298*) Reserva_12998						AT%MX0.9: BOOL;
		(*01x12299*) Reserva_12999						AT%MX0.10: BOOL;
		(*01x12300*) Reserva_12300						AT%MX0.11: BOOL;
		(*01x12301*) Reserva_12301						AT%MX0.12: BOOL;
		(*01x12302*) Reserva_12302						AT%MX0.13: BOOL;
		(*01x12303*) Reserva_12303						AT%MX0.14: BOOL;
		(*01x12304*) Reserva_12304						AT%MX0.15: BOOL;

		(*Modo Automático*)
		(*01x12305*) ModoAuto_Reset						AT%MX1.0: BOOL;
		(*01x12306*) ModoAuto_SelecionaAlvoUP 			AT%MX1.1: BOOL;
		(*01x12307*) ModoAuto_SelecionaAlvoUPGM		AT%MX1.2: BOOL;
		(*01x12308*) ModoAuto_SelecionaAlvoUMD		AT%MX1.3: BOOL;
		(*01x12309*) ModoAuto_SelecionaAlvoUPS			AT%MX1.4: BOOL;
		(*01x12310*) ModoAuto_SelecionaAlvoUS			AT%MX1.5:BOOL;
		(*01x12311*) Reserva_12311						AT%MX1.6: BOOL;
		(*01x12312*) Reserva_12312						AT%MX1.7: BOOL;
		(*01x12313*) Reserva_12313						AT%MX1.8: BOOL;
		(*01x12314*) Reserva_12314						AT%MX1.9: BOOL;
		(*01x12315*) Reserva_12315						AT%MX1.10: BOOL;
		(*01x12316*) Reserva_12316						AT%MX1.11: BOOL;
		(*01x12317*) Reserva_12317						AT%MX1.12: BOOL;
		(*01x12318*) Reserva_12318						AT%MX1.13: BOOL;
		(*01x12319*) Reserva_12319						AT%MX1.14: BOOL;
		(*01x12320*) Reserva_12320						AT%MX1.15: BOOL;

		(*Controle de Potência*)
		(*01x12321*) CtrlP_Ligar 							AT%MX2.0:BOOL;
		(*01x12322*) CtrlP_Desligar 							AT%MX2.1: BOOL;
		(*01x12323*) CtrlP_ReligamentoLigar				AT%MX2.2: BOOL;
		(*01x12324*) CtrlP_ReligamentoDesligar			AT%MX2.3: BOOL;
		(*01x12325*) CtrlQ_ModoFPLigar					AT%MX2.4: BOOL;
		(*01x12326*) CtrlQ_ModoFPDesligar				AT%MX2.5: BOOL;
		(*01x12327*) CtrlQ_ModoVARLigar					AT%MX2.6: BOOL;
		(*01x12328*) CtrlQ_ModoVARDesligar				AT%MX2.7: BOOL;
		(*01x12329*) CtrlU_CmdModoReativo				AT%MX2.8: BOOL;
		(*01x12330*) CtrlU_CmdModoFP					AT%MX2.9:BOOL;
		(*01x12331*) CtrlU_CmdModoManual				AT%MX2.10:BOOL;
		(*01x12332*) Reserva_12332						AT%MX2.11: BOOL;
		(*01x12333*) Reserva_12333						AT%MX2.12: BOOL;
		(*01x12334*) Reserva_12334						AT%MX2.13: BOOL;
		(*01x12335*) Reserva_12335						AT%MX2.14: BOOL;
		(*01x12336*) Reserva_12336						AT%MX2.15: BOOL;
		(*01x12337*) Reserva_12337						AT%MX3.0: BOOL;
		(*01x12338*) Reserva_12338						AT%MX3.1: BOOL;
		(*01x12339*) Reserva_12339						AT%MX3.2: BOOL;
		(*01x12340*) Reserva_12340						AT%MX3.3: BOOL;
		(*01x12341*) Reserva_12341						AT%MX3.4: BOOL;
		(*01x12342*) Reserva_12342						AT%MX3.5: BOOL;
		(*01x12343*) Reserva_12343						AT%MX3.6: BOOL;
		(*01x12344*) Reserva_12344						AT%MX3.7: BOOL;
		(*01x12345*) Reserva_12345						AT%MX3.8: BOOL;
		(*01x12346*) Reserva_12346						AT%MX3.9: BOOL;
		(*01x12347*) Reserva_12347						AT%MX3.10: BOOL;
		(*01x12348*) Reserva_12348						AT%MX3.11: BOOL;
		(*01x12349*) Reserva_12349						AT%MX3.12: BOOL;
		(*01x12350*) Reserva_12350						AT%MX3.13: BOOL;
		(*01x12351*) Reserva_12351						AT%MX3.14: BOOL;
		(*01x12352*) Reserva_12352						AT%MX3.15: BOOL;

		(*UHLM - Unidade Hidráulica de Lubrificação de Mancais*)
		(*01x12353*) UHLM_Bomba01_Ligar							AT%MX4.0:BOOL;
		(*01x12354*) UHLM_Bomba01_Desligar						AT%MX4.1:BOOL;
		(*01x12355*) UHLM_Bomba02_Ligar							AT%MX4.2:BOOL;
		(*01x12356*) UHLM_Bomba02_Desligar						AT%MX4.3: BOOL;
		(*01x12357*) UHLM_ResAquec_Ligar							AT%MX4.4: BOOL;
		(*01x12358*) UHLM_ResAquec_Desligar						AT%MX4.5: BOOL;
		(*01x12359*) UHLM_TrocCalor_Bomba01_Ligar				AT%MX4.6: BOOL;
		(*01x12360*) UHLM_TrocCalor_Bomba01_Desligar			AT%MX4.7: BOOL;
		(*01x12361*) UHLM_Jacking_Ligar								AT%MX4.8: BOOL;
		(*01x12362*) UHLM_Jacking_Desligar							AT%MX4.9: BOOL;
		(*01x12363*) UHLM_SelecaoBomba01_Principal				AT%MX4.10: BOOL;
		(*01x12364*) UHLM_SelecaoBomba02_Principal				AT%MX4.11: BOOL;
		(*01x12365*) UHLM_RodizioManual								AT%MX4.12: BOOL;
		(*01x12366*) UHLM_RodizioAutomatico							AT%MX4.13: BOOL;
		(*01x12367*) Reserva_12367									AT%MX4.14: BOOL;
		(*01x12368*) Reserva_12368									AT%MX4.15: BOOL;

		(*UHRV - Unidade Hidráulica de Regulação de Velocidade*)
		(*01x12369*) UHRV_Bomba01_Ligar				AT%MX5.0: BOOL;
		(*01x12370*) UHRV_Bomba01_Desligar			AT%MX5.1: BOOL;
		(*01x12371*) UHRV_Bomba02_Ligar				AT%MX5.2: BOOL;
		(*01x12372*) UHRV_Bomba02_Desligar			AT%MX5.3: BOOL;
		(*01x12373*) UHRV_ForcarPressurizacao			AT%MX5.4: BOOL;
		(*01x12374*) UHRV_ResAquec_Ligar				AT%MX5.5:BOOL;
		(*01x12375*) UHRV_ResAquec_Desligar			AT%MX5.6:BOOL;
		(*01x12376*) UHRV_SelecaoBomba01_Principal	AT%MX5.7:BOOL;
		(*01x12377*) UHRV_SelecaoBomba02_Principal	AT%MX5.8: BOOL;
		(*01x12378*) UHRV_RodizioManual					AT%MX5.9: BOOL;
		(*01x12379*) UHRV_RodizioAutomatico				AT%MX5.10: BOOL;
		(*01x12380*) Reserva_12380						AT%MX5.11: BOOL;
		(*01x12381*) Reserva_12381						AT%MX5.12: BOOL;
		(*01x12382*) Reserva_12382						AT%MX5.13: BOOL;
		(*01x12383*) Reserva_12383						AT%MX5.14: BOOL;
		(*01x12384*) Reserva_12384						AT%MX5.15: BOOL;
		(*01x12385*) Reserva_12385						AT%MX6.0: BOOL;
		(*01x12386*) Reserva_12386						AT%MX6.1: BOOL;
		(*01x12387*) Reserva_12387						AT%MX6.2: BOOL;
		(*01x12388*) Reserva_12388						AT%MX6.3: BOOL;
		(*01x12389*) Reserva_12389						AT%MX6.4: BOOL;
		(*01x12390*) Reserva_12390						AT%MX6.5: BOOL;
		(*01x12391*) Reserva_12391						AT%MX6.6: BOOL;
		(*01x12392*) Reserva_12392						AT%MX6.7: BOOL;
		(*01x12393*) Reserva_12393						AT%MX6.8: BOOL;
		(*01x12394*) Reserva_12394						AT%MX6.9: BOOL;
		(*01x12395*) Reserva_12395						AT%MX6.10: BOOL;
		(*01x12396*) Reserva_12396						AT%MX6.11: BOOL;
		(*01x12397*) Reserva_12397						AT%MX6.12: BOOL;
		(*01x12398*) Reserva_12398						AT%MX6.13: BOOL;
		(*01x12399*) Reserva_12399						AT%MX6.14: BOOL;
		(*01x12400*) Reserva_12400						AT%MX6.15: BOOL;

		(*Sistema de Filtragem de Água*)
		(*01x12401*) SFA_Bomba01_Ligar					AT%MX7.0: BOOL;
		(*01x12402*) SFA_Bomba01_Desligar				AT%MX7.1: BOOL;
		(*01x12403*) SFA_Bomba02_Ligar					AT%MX7.2:BOOL;
		(*01x12404*) SFA_Bomba03_Desligar				AT%MX7.3:BOOL;
		(*01x12405*) Reserva_12405						AT%MX7.4:BOOL;
		(*01x12406*) Reserva_12406						AT%MX7.5:BOOL;
		(*01x12407*) Reserva_12407						AT%MX7.6: BOOL;
		(*01x12408*) Reserva_12408						AT%MX7.7: BOOL;
		(*01x12409*) Reserva_12409						AT%MX7.8: BOOL;
		(*01x12410*) Reserva_12410						AT%MX7.9: BOOL;
		(*01x12411*) Reserva_12411						AT%MX7.10: BOOL;
		(*01x12412*) Reserva_12412						AT%MX7.11: BOOL;
		(*01x12413*) Reserva_12413						AT%MX7.12: BOOL;
		(*01x12414*) Reserva_12414						AT%MX7.13: BOOL;
		(*01x12415*) Reserva_12415						AT%MX7.14: BOOL;
		(*01x12416*) Reserva_12416						AT%MX7.15: BOOL;

		(*Turbina*)
		(*01x12417*) Turbina_ByPass_Abrir					AT%MX8.0:BOOL;
		(*01x12418*) Turbina_ByPass_Fechar				AT%MX8.1:BOOL;
		(*01x12419*) Turbina_Borboleta_Abrir				AT%MX8.2:BOOL;
		(*01x12420*) Turbina_Borboleta_Fechar			AT%MX8.3:BOOL;
		(*01x12421*) Turbina_Freio_Habilitar				AT%MX8.4: BOOL;
		(*01x12422*) Turbina_Freio_Desabilitar				AT%MX8.5: BOOL;
		(*01x12423*) Reserva_12423						AT%MX8.6: BOOL;
		(*01x12424*) Reserva_12424						AT%MX8.7: BOOL;
		(*01x12425*) Reserva_12425						AT%MX8.8: BOOL;
		(*01x12426*) Reserva_12426						AT%MX8.9: BOOL;
		(*01x12427*) Reserva_12427						AT%MX8.10: BOOL;
		(*01x12428*) Reserva_12428						AT%MX8.11: BOOL;
		(*01x12429*) Reserva_12429						AT%MX8.12: BOOL;
		(*01x12430*) Reserva_12430						AT%MX8.13: BOOL;
		(*01x12431*) Reserva_12431						AT%MX8.14: BOOL;
		(*01x12432*) Reserva_12432						AT%MX8.15: BOOL;

		(*Regulador de Velocidade*)
		(*01x12433*) RegV_Start								AT%MX9.0:BOOL;
		(*01x12434*) RegV_Stop								AT%MX9.1:BOOL;
		(*01x12435*) RegV_Load							AT%MX9.2: BOOL;
		(*01x12436*) RegV_Unload							AT%MX9.3: BOOL;
		(*01x12427*) RegV_IncLoad							AT%MX9.4: BOOL;
		(*01x12438*) RegV_DecLoad						AT%MX9.5: BOOL;
		(*01x12439*) RegV_IncrementaVelocidade			AT%MX9.6: BOOL;
		(*01x12440*) RegV_DecrementaVelocidade		AT%MX9.7: BOOL;
		(*01x12441*) RegV_Ctrl_Man_Distribuidor 			AT%MX9.8: BOOL;
		(*01x12442*) RegV_Ctrl_Man_ValvDistr				AT%MX9.9: BOOL;
		(*01x12443*) RegV_Ctrl_Man_Rotor					AT%MX9.10: BOOL;
		(*01x12444*) RegV_Ctrl_Man_ValvRotor				AT%MX9.11: BOOL;
		(*01x12445*) RegV_Ctrl_Velocidade					AT%MX9.12: BOOL;
		(*01x12446*) RegV_ModoEstatismo					AT%MX9.13: BOOL;
		(*01x12447*) RegV_ModoBase_Carga				AT%MX9.14: BOOL;
		(*01x12448*) RegV_Compensacao_PotP			AT%MX9.15: BOOL;

		(*01x12449*) RegV_Ctrl_PotP						AT%MX10.0:BOOL;
		(*01x12450*) Reserva_12450						AT%MX10.1:BOOL;
		(*01x12451*) Reserva_12451						AT%MX10.2: BOOL;
		(*01x12452*) Reserva_12452						AT%MX10.3: BOOL;
		(*01x12453*) Reserva_12453						AT%MX10.4: BOOL;
		(*01x12454*) Reserva_12454						AT%MX10.5: BOOL;
		(*01x12455*) Reserva_12455						AT%MX10.6: BOOL;
		(*01x12456*) Reserva_12456						AT%MX10.7: BOOL;
		(*01x12457*) Reserva_12457 						AT%MX10.8: BOOL;
		(*01x12458*) Reserva_12458						AT%MX10.9: BOOL;
		(*01x12459*) Reserva_12459						AT%MX10.10: BOOL;
		(*01x12460*) Reserva_12460						AT%MX10.11: BOOL;
		(*01x12461*) Reserva_12461						AT%MX10.12: BOOL;
		(*01x12462*) Reserva_12462						AT%MX10.13: BOOL;
		(*01x12463*) Reserva_12463						AT%MX10.14: BOOL;
		(*01x12464*) Reserva_12464						AT%MX10.15: BOOL;

		(*Regulador de Tensão*)
		(*01x12465*) RegT_Ligar							AT%MX11.0: BOOL;
		(*01x12466*) RegT_Desligar							AT%MX11.1: BOOL;
		(*01x12467*) RegT_IncrementaTensao				AT%MX11.2: BOOL;
		(*01x12468*) RegT_DecrementaTensao			AT%MX11.3: BOOL;
		(*01x12469*) RegT_Liga_PreExcitacao				AT%MX11.4: BOOL;
		(*01x12470*) RegT_Desliga_PreExcitacao			AT%MX11.5: BOOL;
		(*01x12471*) RegT_Ctrl_Tensao						AT%MX11.6: BOOL;
		(*01x12472*) RegT_Ctrl_FP							AT%MX11.7: BOOL;
		(*01x12473*) RegT_Ctrl_VAR						AT%MX11.8: BOOL;
		(*01x12474*) Reserva_12474						AT%MX11.9: BOOL;
		(*01x12475*) Reserva_12475						AT%MX11.10: BOOL;
		(*01x12476*) Reserva_12476						AT%MX11.11: BOOL;
		(*01x12477*) Reserva_12477						AT%MX11.12: BOOL;
		(*01x12478*) Reserva_12478						AT%MX11.13: BOOL;
		(*01x12479*) Reserva_12479						AT%MX11.14: BOOL;
		(*01x12480*) Reserva_12480						AT%MX11.15: BOOL;

		(*Sincronismo*)
		(*01x12481*) SincAuto_Ligar							AT%MX12.0: BOOL;
		(*01x12482*) SincAuto_Desligar						AT%MX12.1:BOOL;
		(*01x12483*) SincManual_Ligar						AT%MX12.2:BOOL;
		(*01x12484*) SincManual_Desligar					AT%MX12.3:BOOL;
		(*01x12485*) SincBM_Ligar							AT%MX12.4:BOOL;
		(*01x12486*) SincBMl_Desligar						AT%MX12.5:BOOL;
		(*01x12487*) Reserva_12487						AT%MX12.6: BOOL;
		(*01x12488*) Reserva_12488						AT%MX12.7: BOOL;
		(*01x12489*) Reserva_12489						AT%MX12.8: BOOL;
		(*01x12490*) Reserva_12490						AT%MX12.9: BOOL;
		(*01x12491*) Reserva_12491						AT%MX12.10: BOOL;
		(*01x12492*) Reserva_12492						AT%MX12.11: BOOL;
		(*01x12493*) Reserva_12493						AT%MX12.12: BOOL;
		(*01x12494*) Reserva_12494						AT%MX12.13: BOOL;
		(*01x12495*) Reserva_12495						AT%MX12.14: BOOL;
		(*01x12496*) Reserva_12496						AT%MX12.15: BOOL;

		(*Relésde Bloqueio*)
		(*01x12497*) Rele86M_Atuar							AT%MX13.0:BOOL;
		(*01x12498*) Rele86E_Atuar							AT%MX13.1:BOOL;
		(*01x12499*) Rele86H_Atuar							AT%MX13.2:BOOL;
		(*01x12500*) Rejeicao_86E							AT%MX13.3:BOOL;
		(*01x12501*) Rejeicao_86H							AT%MX13.4:BOOL;
		(*01x12502*) Reserva_12502						AT%MX13.5:BOOL;
		(*01x12503*) Reserva_12503						AT%MX13.6: BOOL;
		(*01x12504*) Reserva_12504						AT%MX13.7: BOOL;
		(*01x12505*) Reserva_12505						AT%MX13.8: BOOL;
		(*01x12506*) Reserva_12506						AT%MX13.9: BOOL;
		(*01x12507*) Reserva_12507						AT%MX13.10: BOOL;
		(*01x12508*) Reserva_12508						AT%MX13.11: BOOL;
		(*01x12509*) Reserva_12509						AT%MX13.12: BOOL;
		(*01x12510*) Reserva_12510						AT%MX13.13: BOOL;
		(*01x12511*) Reserva_12511						AT%MX13.14: BOOL;
		(*01x12512*) Reserva_12512						AT%MX13.15: BOOL;

		(*Analógicas*)

		(*Disjuntor 52G*)
		(*01x12513*) Disj52G_Abrir							AT%MX14.0:BOOL;
		(*01x12514*) Reserva_12514						AT%MX14.1:BOOL;
		(*01x12515*) Reserva_12515						AT%MX14.2:BOOL;
		(*01x12516*) Reserva_12516						AT%MX14.3:BOOL;
		(*01x12517*) Reserva_12517						AT%MX14.4:BOOL;
		(*01x12518*) Reserva_12518						AT%MX14.5:BOOL;
		(*01x12519*) Reserva_12519						AT%MX14.6: BOOL;
		(*01x12520*) Reserva_12520						AT%MX14.7: BOOL;
		(*01x12521*) Reserva_12521						AT%MX14.8: BOOL;
		(*01x12522*) Reserva_12522						AT%MX14.9: BOOL;
		(*01x12523*) Reserva_12523						AT%MX14.10: BOOL;
		(*01x12524*) Reserva_12524						AT%MX14.11: BOOL;
		(*01x12525*) Reserva_12525						AT%MX14.12: BOOL;
		(*01x12526*) Reserva_12526						AT%MX14.13: BOOL;
		(*01x12527*) Reserva_12527						AT%MX14.14: BOOL;
		(*01x12528*) Reserva_12528						AT%MX14.15: BOOL;

		(*Disjuntores Auxilares*)

		(*Vibracao*)

		(*Relé de Proteção*)

		(*Reset Alarmes*)
		(*01x12529*) Reset_SuperSEP						AT%MX15.0: BOOL;
		(*01x12530*) Reset_Local							AT%MX15.1: BOOL;
		(*01x12531*) CalaSirene_SuperSEP				AT%MX15.2:BOOL;
		(*01x12532*) CalaSirene_Local						AT%MX15.3:BOOL;
		(*01x12533*) Reserva_12533						AT%MX15.4:BOOL;
		(*01x12534*) Reserva_12534						AT%MX15.5:BOOL;
		(*01x12535*) Reserva_12535						AT%MX15.6: BOOL;
		(*01x12536*) Reserva_12536						AT%MX15.7: BOOL;
		(*01x12537*) Reserva_12537						AT%MX15.8: BOOL;
		(*01x12538*) Reserva_12538						AT%MX15.9: BOOL;
		(*01x12539*) Reserva_12539						AT%MX15.10: BOOL;
		(*01x12540*) Reserva_12540						AT%MX15.11: BOOL;
		(*01x12541*) Reserva_12541						AT%MX15.12: BOOL;
		(*01x12542*) Reserva_12542						AT%MX15.13: BOOL;
		(*01x12543*) Reserva_12543						AT%MX15.14: BOOL;
		(*01x12544*) Reserva_12544						AT%MX15.15: BOOL;

		(*Totalizador de Potência*)
		(*01x12545*) Reset_AcumuladorEnergia			AT%MX16.0: BOOL;
		(*01x12546*) Reserva_12546						AT%MX16.1: BOOL;
		(*01x12547*) Reserva_12547						AT%MX16.2:BOOL;
		(*01x12548*) Reserva_12548						AT%MX16.3:BOOL;
		(*01x12549*) Reserva_12549						AT%MX16.4:BOOL;
		(*01x12550*) Reserva_12550						AT%MX16.5:BOOL;
		(*01x12551*) Reserva_12551						AT%MX16.6: BOOL;
		(*01x12552*) Reserva_12552						AT%MX16.7: BOOL;
		(*01x12553*) Reserva_12553						AT%MX16.8: BOOL;
		(*01x12554*) Reserva_12554						AT%MX16.9: BOOL;
		(*01x12555*) Reserva_12555						AT%MX16.10: BOOL;
		(*01x12556*) Reserva_12556						AT%MX16.11: BOOL;
		(*01x12557*) Reserva_12557						AT%MX16.12: BOOL;
		(*01x12558*) Reserva_12558						AT%MX16.13: BOOL;
		(*01x12559*) Reserva_12559						AT%MX16.14: BOOL;
		(*01x12560*) Reserva_12560						AT%MX16.15: BOOL;

		(*Temperaturas*)
		(*01x12561*) AR1_RTD1_Block_Protecao			AT%MX17.0:BOOL;
		(*01x12562*) AR1_RTD2_Block_Protecao			AT%MX17.1:BOOL;
		(*01x12563*) AR1_RTD3_Block_Protecao			AT%MX17.2:BOOL;
		(*01x12564*) AR1_RTD4_Block_Protecao			AT%MX17.3:BOOL;
		(*01x12565*) AR2_RTD1_Block_Protecao			AT%MX17.4: BOOL;
		(*01x12566*) AR2_RTD2_Block_Protecao			AT%MX17.5: BOOL;
		(*01x12567*) AR2_RTD3_Block_Protecao			AT%MX17.6: BOOL;
		(*01x12568*) AR2_RTD4_Block_Protecao			AT%MX17.7: BOOL;
		(*01x12569*) AR3_RTD1_Block_Protecao			AT%MX17.8: BOOL;
		(*01x12570*) AR3_RTD2_Block_Protecao			AT%MX17.9: BOOL;
		(*01x12571*) AR3_RTD3_Block_Protecao			AT%MX17.10: BOOL;
		(*01x12572*) AR3_RTD4_Block_Protecao			AT%MX17.11: BOOL;
		(*01x12573*) AR4_RTD1_Block_Protecao			AT%MX17.12: BOOL;
		(*01x12574*) AR4_RTD2_Block_Protecao			AT%MX17.13: BOOL;
		(*01x12575*) AR4_RTD3_Block_Protecao			AT%MX17.14: BOOL;
		(*01x12576*) AR4_RTD4_Block_Protecao			AT%MX17.15: BOOL;
		(*01x12577*) AR5_RTD1_Block_Protecao			AT%MX18.0:BOOL;
		(*01x12578*) AR5_RTD2_Block_Protecao			AT%MX18.1:BOOL;
		(*01x12579*) AR5_RTD3_Block_Protecao			AT%MX18.2:BOOL;
		(*01x12580*) AR5_RTD4_Block_Protecao			AT%MX18.3:BOOL;
		(*01x12581*) AR6_RTD1_Block_Protecao			AT%MX18.4: BOOL;
		(*01x12582*) AR6_RTD2_Block_Protecao			AT%MX18.5: BOOL;
		(*01x12583*) AR6_RTD3_Block_Protecao			AT%MX18.6: BOOL;
		(*01x12584*) AR6_RTD4_Block_Protecao			AT%MX18.7: BOOL;
		(*01x12585*) AR7_RTD1_Block_Protecao			AT%MX18.8: BOOL;
		(*01x12586*) AR7_RTD2_Block_Protecao			AT%MX18.9: BOOL;
		(*01x12587*) AR7_RTD3_Block_Protecao			AT%MX18.10: BOOL;
		(*01x12588*) AR7_RTD4_Block_Protecao			AT%MX18.11: BOOL;
		(*01x12589*) AR8_RTD1_Block_Protecao			AT%MX18.12: BOOL;
		(*01x12590*) AR8_RTD2_Block_Protecao			AT%MX18.13: BOOL;
		(*01x12591*) AR8_RTD3_Block_Protecao			AT%MX18.14: BOOL;
		(*01x12592*) AR8_RTD4_Block_Protecao			AT%MX18.15: BOOL;

		(*Monitor Barragem*)
		(*01x12593*) NivelHH_Block_Protecao				AT%MX19.0:BOOL;
		(*01x12594*) NivelH_Block_Protecao				AT%MX19.1:BOOL;
		(*01x12595*) NivelLL_Block_Protecao				AT%MX19.2:BOOL;
		(*01x12596*) NivelL_Block_Protecao				AT%MX19.3:BOOL;
		(*01x12597*) Reserva_125978						AT%MX19.4: BOOL;
		(*01x12598*) Reserva_125988						AT%MX19.5: BOOL;
		(*01x12599*) Reserva_125998						AT%MX19.6: BOOL;
		(*01x12600*) Reserva_126008						AT%MX19.7: BOOL;
		(*01x12601*) Reserva_12601						AT%MX19.8: BOOL;
		(*01x12602*) Reserva_12602						AT%MX19.9: BOOL;
		(*01x12603*) Reserva_12603						AT%MX19.10: BOOL;
		(*01x12604*) Reserva_12604						AT%MX19.11: BOOL;
		(*01x12605*) Reserva_12605						AT%MX19.12: BOOL;
		(*01x12606*) Reserva_12606						AT%MX19.13: BOOL;
		(*01x12607*) Reserva_12607						AT%MX19.14: BOOL;
		(*01x12608*) Reserva_12608						AT%MX19.15: BOOL;

		(*Horímetro*)
		(*01x12609*) Reset_HorimetroEletrico				AT%MX20.0: BOOL;
		(*01x12610*) Reset_HorimetroMecanico			AT%MX20.1: BOOL;
		(*01x12611*) Reset_HorimetroUHRV				AT%MX20.2:BOOL;
		(*01x12612*) Reset_HorimetroUHLM				AT%MX20.3:BOOL;
		(*01x12613*) Reserva_12613						AT%MX20.4: BOOL;
		(*01x12614*) Reserva_12614						AT%MX20.5: BOOL;
		(*01x12615*) Reserva_12615						AT%MX20.6: BOOL;
		(*01x12616*) Reserva_12616						AT%MX20.7: BOOL;
		(*01x12617*) Reserva_12617						AT%MX20.8: BOOL;
		(*01x12618*) Reserva_12618						AT%MX20.9: BOOL;
		(*01x12619*) Reserva_12619						AT%MX20.10: BOOL;
		(*01x12620*) Reserva_12620						AT%MX20.11: BOOL;
		(*01x12621*) Reserva_12621						AT%MX20.12: BOOL;
		(*01x12622*) Reserva_12622						AT%MX20.13: BOOL;
		(*01x12623*) Reserva_12623						AT%MX20.14: BOOL;
		(*01x12624*) Reserva_12624						AT%MX20.15: BOOL;

		(*Mapa Lógico*)
		(*01x12641*) QTA_Comporta01_Abrir					AT%MX22.0:BOOL;
		(*01x12642*) QTA_Comporta01_Fechar 				AT%MX22.1:BOOL;
		(*01x12643*) QTA_Comporta02_Abrir					AT%MX22.2:BOOL;
		(*01x12644*) QTA_Comporta02_Fechar 				AT%MX22.3:BOOL;
		(*01x12645*) QTA_Comporta03_Abrir					AT%MX22.4: BOOL;
		(*01x12646*) QTA_Comporta03_Fechar					AT%MX22.5: BOOL;
		(*01x12647*) Reserva_12647							AT%MX22.6: BOOL;
		(*01x12648*) Reserva_12648							AT%MX22.7: BOOL;
		(*01x12649*) Reserva_12649							AT%MX22.8: BOOL;
		(*01x12650*) Reserva_12650							AT%MX22.9: BOOL;
		(*01x12651*) Reserva_12651							AT%MX22.10: BOOL;
		(*01x12652*) Reserva_12652							AT%MX22.11: BOOL;
		(*01x12653*) Reserva_12653							AT%MX22.12: BOOL;
		(*01x12654*) Reserva_12654							AT%MX22.13: BOOL;
		(*01x12655*) Reserva_12655							AT%MX22.14: BOOL;
		(*01x12656*) Reserva_12656							AT%MX22.15: BOOL;
'''
status = '''


		(*Painel de Controle*)
		(*01x20289*) Operacao_Emergencia_Local							AT%MX500.0:  BOOL;
		(*01x20290*) Operacao_Emergencia_SuperSEP						AT%MX500.1:  BOOL;
		(*01x20291*) Operacao_Emergencia_UHRV							AT%MX500.2:  BOOL;
		(*01x20292*) Operacao_Emergencia_UHLM							AT%MX500.3:  BOOL;
		(*01x20293*) Operacao_ModoAuto										AT%MX500.4:  BOOL;
		(*01x20294*) Operacao_ModoManual									AT%MX500.5:  BOOL;
		(*01x20295*) Operacao_PartidaReligamento							AT%MX500.6:  BOOL;
		(*01x20296*) Operacao_PartidaManual									AT%MX500.7:  BOOL;
		(*01x20297*) Operacao_ParadaTripAgua								AT%MX500.8:  BOOL;
		(*01x20298*) Operacao_ParadaTripEletrico								AT%MX500.9:  BOOL;
		(*01x20299*) Operacao_ParadaTripMecanico							AT%MX500.10:  BOOL;
		(*01x20300*) Operacao_ParadaTripHidraulico							AT%MX500.11:  BOOL;
		(*01x20301*) Operacao_ParadaNormal									AT%MX500.12:  BOOL;
		(*01x20302*) Operacao_ParadaEmergenciaLocal						AT%MX500.13:  BOOL;
		(*01x20303*) Operacao_ParadaEmergenciaSuperSEP				AT%MX500.14:  BOOL;
		(*01x20304*) Operacao_ParadaEmergenciaUHRV						AT%MX500.15:  BOOL;
		(*01x20305*) Operacao_ParadaEmergenciaUHLM						AT%MX501.0:  BOOL;
		(*01x20306*) Operacao_ParadaAbertura52G							AT%MX501.1:  BOOL;
		(*01x20307*) Operacao_ParadaInfoValida								AT%MX501.2:  BOOL;
		(*01x20308*) Operacao_BloqueioAtuado								AT%MX501.3:  BOOL;
		(*01x20309*) Operacao_PresencaTensao								AT%MX501.4:  BOOL;
		(*01x20310*) Reserva_20310											AT%MX501.5:  BOOL;
		(*01x20311*) Reserva_20311											AT%MX501.6:  BOOL;
		(*01x20312*) Reserva_20312											AT%MX501.7:  BOOL;
		(*01x20313*) Reserva_20313											AT%MX501.8:  BOOL;
		(*01x20314*) Reserva_20314											AT%MX501.9:  BOOL;
		(*01x20315*) Reserva_20315											AT%MX501.10:  BOOL;
		(*01x20316*) Reserva_20316											AT%MX501.11:  BOOL;
		(*01x20317*) Reserva_20317											AT%MX501.12:  BOOL;
		(*01x20318*) Reserva_20318											AT%MX501.13:  BOOL;
		(*01x20319*) Reserva_20319											AT%MX501.14:  BOOL;
		(*01x20320*) Reserva_20320											AT%MX501.15:  BOOL;

		(*Modo Automático*)
		(*01x20321*) ModoAuto_AlvoUP											AT%MX502.0:  BOOL;
		(*01x20322*) ModoAuto_AlvoUPGM										AT%MX502.1:  BOOL;
		(*01x20323*) ModoAuto_AlvoUMD										AT%MX502.2:  BOOL;
		(*01x20324*) ModoAuto_AlvoUPS										AT%MX502.3:  BOOL;
		(*01x20325*) ModoAuto_AlvoUS											AT%MX502.4:  BOOL;
		(*01x20326*) ModoAuto_UP												AT%MX502.5:  BOOL;
		(*01x20327*) ModoAuto_UPGM											AT%MX502.6:  BOOL;
		(*01x20328*) ModoAuto_UMD											AT%MX502.7:  BOOL;
		(*01x20329*) ModoAuto_UPS											AT%MX502.8:  BOOL;
		(*01x20330*) ModoAuto_US												AT%MX502.9:  BOOL;
		(*01x20331*) ModoAuto_Transicao										AT%MX502.10:  BOOL;
		(*01x20332*) ModoAuto_TransicaoUPtoUPGM							AT%MX502.11:  BOOL;
		(*01x20333*) ModoAuto_TransicaoUPGMtoUMD						AT%MX502.12:  BOOL;
		(*01x20334*) ModoAuto_TransicaoUMDtoUPS							AT%MX502.13:  BOOL;
		(*01x20335*) ModoAuto_TransicaoUPStoUS							AT%MX502.14:  BOOL;
		(*01x20336*) ModoAuto_TransicaoUStoUPS							AT%MX502.15:  BOOL;
		(*01x20337*) ModoAuto_TransicaoUPStoUMD							AT%MX503.0:  BOOL;
		(*01x20338*) ModoAuto_TransicaoUMDtoUPGM						AT%MX503.1:  BOOL;
		(*01x20339*) ModoAuto_TransicaoUPGMtoUP							AT%MX503.2:  BOOL;
		(*01x20340*) Reserva_28340											AT%MX503.3:  BOOL;
		(*01x20341*) Reserva_28341											AT%MX503.4:  BOOL;
		(*01x20342*) Reserva_28342											AT%MX503.5:  BOOL;
		(*01x20343*) Reserva_28343											AT%MX503.6:  BOOL;
		(*01x20344*) Reserva_28344											AT%MX503.7:  BOOL;
		(*01x20345*) Reserva_28345											AT%MX503.8:  BOOL;
		(*01x20346*) Reserva_28346											AT%MX503.9:  BOOL;
		(*01x20347*) Reserva_28347											AT%MX503.10:  BOOL;
		(*01x20348*) Reserva_28348											AT%MX503.11:  BOOL;
		(*01x20349*) Reserva_13149											AT%MX503.12:  BOOL;
		(*01x20350*) Reserva_28350											AT%MX503.13:  BOOL;
		(*01x20351*) Reserva_28351											AT%MX503.14:  BOOL;
		(*01x20352*) Reserva_28352											AT%MX503.15:  BOOL;

		(*Controle de Potência*)
		(*01x20353*) CtrlP_Status												AT%MX504.0:  BOOL;
		(*01x20354*) CtrlP_Religamento										AT%MX504.1:  BOOL;
		(*01x20355*) CtrlQ_ModoFP												AT%MX504.2:  BOOL;
		(*01x20356*) CtrlQ_ModoVAr												AT%MX504.3:  BOOL;
		(*01x20357*) Reserva_20357											AT%MX504.4:  BOOL;
		(*01x20358*) Reserva_20358											AT%MX504.5:  BOOL;
		(*01x20359*) Reserva_20359											AT%MX504.6:  BOOL;
		(*01x20360*) Reserva_20360											AT%MX504.7:  BOOL;
		(*01x20361*) Reserva_20361											AT%MX504.8:  BOOL;
		(*01x20362*) Reserva_20362											AT%MX504.9:  BOOL;
		(*01x20363*) Reserva_20363											AT%MX504.10:  BOOL;
		(*01x20364*) Reserva_20364											AT%MX504.11:  BOOL;
		(*01x20365*) Reserva_20365											AT%MX504.12:  BOOL;
		(*01x20366*) Reserva_20366											AT%MX504.13:  BOOL;
		(*01x20367*) Reserva_20367											AT%MX504.14:  BOOL;
		(*01x20368*) Reserva_20368											AT%MX504.15:  BOOL;

		(*UHLM*)
		(*01x20369*) UHLM_Ligada												AT%MX505.0:  BOOL;
		(*01x20370*) UHLM_Desligada											AT%MX505.1:  BOOL;
		(*01x20371*) UHLM_Operacional										AT%MX505.2:  BOOL;
		(*01x20372*) UHLM_Bomba01_Status									AT%MX505.3:  BOOL;
		(*01x20373*) UHLM_Bomba02_Status									AT%MX505.4:  BOOL;
		(*01x20374*) UHLM_Bomba03_Status									AT%MX505.5:  BOOL;
		(*01x20375*) UHLM_Bomba04_Status									AT%MX505.6:  BOOL;
		(*01x20376*) UHLM_Bomba05_Status									AT%MX505.7:  BOOL;
		(*01x20377*) UHLM_Bomba01_Trip										AT%MX505.8:  BOOL;
		(*01x20378*) UHLM_Bomba02_Trip										AT%MX505.9:  BOOL;
		(*01x20379*) UHLM_Bomba03_Trip										AT%MX505.10:  BOOL;
		(*01x20380*) UHLM_Bomba04_Trip										AT%MX505.11:  BOOL;
		(*01x20381*) UHLM_Bomba05_Trip										AT%MX505.12:  BOOL;
		(*01x20382*) UHLM_Fluxo01_TrocrCalor								AT%MX505.13:  BOOL;
		(*01x20383*) UHLM_Fluxo02_TrocrCalor								AT%MX505.14:  BOOL;
		(*01x20384*) UHLM_Fluxo03_TrocrCalor								AT%MX505.15:  BOOL;
		(*01x20385*) UHLM_Fluxo04_TrocrCalor								AT%MX506.0:  BOOL;
		(*01x20386*) UHLM_Fluxo05_TrocrCalor								AT%MX506.1:  BOOL;
		(*01x20387*) UHLM_FluxoOleo_Mancal01								AT%MX506.2:  BOOL;
		(*01x20388*) UHLM_FluxoOleo_Mancal02								AT%MX506.3:  BOOL;
		(*01x20389*) UHLM_FluxoOleo_Mancal03								AT%MX506.4:  BOOL;
		(*01x20390*) UHLM_FluxoOleo_Mancal04								AT%MX506.5:  BOOL;
		(*01x20391*) UHLM_FluxoOleo_Mancal05								AT%MX506.6:  BOOL;
		(*01x20392*) UHLM_Pressostato01_Linha								AT%MX506.7:  BOOL;
		(*01x20393*) UHLM_Pressostato02_Linha								AT%MX506.8:  BOOL;
		(*01x20394*) UHLM_Pressostato03_Linha								AT%MX506.9:  BOOL;
		(*01x20395*) UHLM_Pressostato04_Linha								AT%MX506.10:  BOOL;
		(*01x20396*) UHLM_Pressostato05_Linha								AT%MX506.11:  BOOL;
		(*01x20397*) UHLM_FiltroOleo01_Sujo									AT%MX506.12:  BOOL;
		(*01x20398*) UHLM_FiltroOleo02_Sujo									AT%MX506.13:  BOOL;
		(*01x20399*) UHLM_FiltroOleo03_Sujo									AT%MX506.14:  BOOL;
		(*01x20400*) UHLM_FiltroOleo04_Sujo									AT%MX506.15:  BOOL;
		(*01x20401*) UHLM_FiltroOleo05_Sujo									AT%MX507.0:  BOOL;
		(*01x20402*) UHLM_NivelMaximo01_Oleo								AT%MX507.1:  BOOL;
		(*01x20403*) UHLM_NivelMaximo02_Oleo								AT%MX507.2:  BOOL;
		(*01x20404*) UHLM_NivelMaximo03_Oleo								AT%MX507.3:  BOOL;
		(*01x20405*) UHLM_NivelMinimo01_Oleo								AT%MX507.4:  BOOL;
		(*01x20406*) UHLM_NivelMinimo02_Oleo								AT%MX507.5:  BOOL;
		(*01x20407*) UHLM_NivelMinimo03_Oleo								AT%MX507.6:  BOOL;
		(*01x20408*)  UHLM_ResAquec_Operacional							AT%MX507.7:  BOOL;
		(*01x20409*)  UHLM_ResAquec_Ligada								AT%MX507.8:  BOOL;
		(*01x20410*)  UHLM_ResAquec_Desligada							AT%MX507.9:  BOOL;
		(*01x20411*)  UHLM_ResAquec_Trip									AT%MX507.10:  BOOL;
		(*01x20412*) TrocCalor_Bomba01_Status								AT%MX507.11:  BOOL;
		(*01x20413*) TrocCalor_Bomba02_Status								AT%MX507.12:  BOOL;
		(*01x20414*) TrocCalor_Bomba03_Status								AT%MX507.13:  BOOL;
		(*01x20415*) TrocCalor_Bomba04_Status								AT%MX507.14:  BOOL;
		(*01x20416*) TrocCalor_Bomba05_Status								AT%MX507.15:  BOOL;
		(*01x20417*) TrocCalor_Bomba01_Trip									AT%MX508.0:  BOOL;
		(*01x20418*) TrocCalor_Bomba02_Trip									AT%MX508.1:  BOOL;
		(*01x20419*) TrocCalor_Bomba03_Trip									AT%MX508.2:  BOOL;
		(*01x20420*) TrocCalor_Bomba04_Trip									AT%MX508.3:  BOOL;
		(*01x20421*) TrocCalor_Bomba05_Trip									AT%MX508.4:  BOOL;
		(*01x20422*) UHLM_TrocCalor_Operacional							AT%MX508.5:  BOOL;
		(*01x20423*) Reserva_20423											AT%MX508.6:  BOOL;
		(*01x20424*) Reserva_20424											AT%MX508.7:  BOOL;
		(*01x20425*) Reserva_20425											AT%MX508.8:  BOOL;
		(*01x20426*) Reserva_20426											AT%MX508.9:  BOOL;
		(*01x20427*) Reserva_20427											AT%MX508.10:  BOOL;
		(*01x20428*) Reserva_20428											AT%MX508.11:  BOOL;
		(*01x20429*) Reserva_20429											AT%MX508.12:  BOOL;
		(*01x20430*) Reserva_20430											AT%MX508.13:  BOOL;
		(*01x20431*) Reserva_20431											AT%MX508.14:  BOOL;
		(*01x20432*) Reserva_20432											AT%MX508.15:  BOOL;

		(*UHRV*)
		(*01x20433*) UHRV_Ligada												AT%MX509.0:  BOOL;
		(*01x20434*) UHRV_Desligada											AT%MX509.1:  BOOL;
		(*01x20435*) UHRV_Operacional										AT%MX509.2:  BOOL;
		(*01x20436*) UHRV_PressaoCritica										AT%MX509.3:  BOOL;
		(*01x20437*) UHRV_Bomba01_Status									AT%MX509.4:  BOOL;
		(*01x20438*) UHRV_Bomba02_Status									AT%MX509.5:  BOOL;
		(*01x20439*) UHRV_Bomba03_Status									AT%MX509.6:  BOOL;
		(*01x20440*) UHRV_Bomba04_Status									AT%MX509.7:  BOOL;
		(*01x20441*) UHRV_Bomba05_Status									AT%MX509.8:  BOOL;
		(*01x20442*) UHRV_Bomba01_Trip										AT%MX509.9:  BOOL;
		(*01x20443*) UHRV_Bomba02_Trip										AT%MX509.10:  BOOL;
		(*01x20444*) UHRV_Bomba03_Trip										AT%MX509.11:  BOOL;
		(*01x20445*) UHRV_Bomba04_Trip										AT%MX509.12:  BOOL;
		(*01x20446*) UHRV_Bomba05_Trip										AT%MX509.13:  BOOL;
		(*01x20447*) UHRV_FiltroPressao01_Sujo								AT%MX509.14:  BOOL;
		(*01x20448*) UHRV_FiltroPressao02_Sujo								AT%MX509.15:  BOOL;
		(*01x20449*) UHRV_FiltroPressao03_Sujo								AT%MX510.0:  BOOL;
		(*01x20450*) UHRV_FiltroPressao04_Sujo								AT%MX510.1:  BOOL;
		(*01x20451*) UHRV_FiltroPressao05_Sujo								AT%MX510.2:  BOOL;
		(*01x20452*) UHRV_FiltroRetorno01_Sujo								AT%MX510.3:  BOOL;
		(*01x20453*) UHRV_FiltroRetorno02_Sujo								AT%MX510.4:  BOOL;
		(*01x20454*) UHRV_FiltroRetorno03_Sujo								AT%MX510.5:  BOOL;
		(*01x20455*) UHRV_FiltroRetorno04_Sujo								AT%MX510.6:  BOOL;
		(*01x20456*) UHRV_FiltroRetorno05_Sujo								AT%MX510.7:  BOOL;
		(*01x20457*) UHRV_NivelMinimo01_Oleo								AT%MX510.8:  BOOL;
		(*01x20458*) UHRV_NivelMinimo02_Oleo								AT%MX510.9:  BOOL;
		(*01x20459*) UHRV_NivelMinimo03_Oleo								AT%MX510.10:  BOOL;
		(*01x20460*) UHRV_NivelMaximo01_Oleo								AT%MX510.11:  BOOL;
		(*01x20461*) UHRV_NivelMaximo02_Oleo								AT%MX510.12:  BOOL;
		(*01x20462*) UHRV_NivelMaximo03_Oleo								AT%MX510.13:  BOOL;
		(*01x20463*) UHRV_Pressostato_Maximo								AT%MX510.14:  BOOL;
		(*01x20464*) UHRV_Pressostato_Minimo								AT%MX510.15:  BOOL;
		(*01x20465*) UHRV_Pressostato_Critico								AT%MX511.0:  BOOL;
		(*01x20466*) UHRV_Pressostato01										AT%MX511.1:  BOOL;
		(*01x20467*) UHRV_Pressostato02										AT%MX511.2:  BOOL;
		(*01x20468*) UHRV_Pressostato03										AT%MX511.3:  BOOL;
		(*01x20469*) UHRV_ResAquec_Ligada									AT%MX511.4:  BOOL;
		(*01x20470*) UHRV_ResAquec_Desligada								AT%MX511.5:  BOOL;
		(*01x20471*) UHRV_ValvCtrl_Pressao01								AT%MX511.6:  BOOL;
		(*01x20472*) UHRV_ValvCtrl_Pressao02								AT%MX511.7:  BOOL;
		(*01x20473*) Reserva_20473											AT%MX511.8:  BOOL;
		(*01x20474*) Reserva_20474											AT%MX511.9:  BOOL;
		(*01x20475*) Reserva_20475											AT%MX511.10:  BOOL;
		(*01x20476*) Reserva_20476											AT%MX511.11:  BOOL;
		(*01x20477*) Reserva_20477											AT%MX511.12:  BOOL;
		(*01x20478*) Reserva_20478											AT%MX511.13:  BOOL;
		(*01x20479*) Reserva_20479											AT%MX511.14:  BOOL;
		(*01x20480*) Reserva_20480											AT%MX511.15:  BOOL;
		(*01x20481*) Reserva_20481											AT%MX512.0:  BOOL;
		(*01x20482*) Reserva_20482											AT%MX512.1:  BOOL;
		(*01x20483*) Reserva_20483											AT%MX512.2:  BOOL;
		(*01x20484*) Reserva_20484											AT%MX512.3:  BOOL;
		(*01x20485*) Reserva_20485											AT%MX512.4:  BOOL;
		(*01x20486*) Reserva_20486											AT%MX512.5:  BOOL;
		(*01x20487*) Reserva_20487											AT%MX512.6:  BOOL;
		(*01x20488*) Reserva_20488											AT%MX512.7:  BOOL;
		(*01x20489*) Reserva_20489											AT%MX512.8:  BOOL;
		(*01x20490*) Reserva_20490											AT%MX512.9:  BOOL;
		(*01x20491*) Reserva_20491											AT%MX512.10:  BOOL;
		(*01x20492*) Reserva_20492											AT%MX512.11:  BOOL;
		(*01x20493*) Reserva_20493											AT%MX512.12:  BOOL;
		(*01x20494*) Reserva_20494											AT%MX512.13:  BOOL;
		(*01x20495*) Reserva_20495											AT%MX512.14:  BOOL;
		(*01x20496*) Reserva_20496											AT%MX512.15:  BOOL;

		(*Sistema de Filtragem de Água*)
		(*01x20497*) SFA_Operacional 											AT%MX513.0: BOOL;
		(*01x20498*) SFA_Ligada												AT%MX513.1:  BOOL;
		(*01x20499*) SFA_Desligada											AT%MX513.2:  BOOL;
		(*01x20500*) SFA_StatusBomba01										AT%MX513.3:  BOOL;
		(*01x20501*) SFA_StatusBomba02										AT%MX513.4:  BOOL;
		(*01x20502*) SFA_TRIPBomba01										AT%MX513.5:  BOOL;
		(*01x20503*) SFA_TRIPBomba02										AT%MX513.6:  BOOL;
		(*01x20504*) SFA_Pressostato01										AT%MX513.7:  BOOL;
		(*01x20505*) SFA_Pressostato02										AT%MX513.8:  BOOL;
		(*01x20506*) SFA_Pressostato03										AT%MX513.9:  BOOL;
		(*01x20507*) Reserva_20507											AT%MX513.10: BOOL;
		(*01x20508*) Reserva_20508											AT%MX513.11: BOOL;
		(*01x20509*) Reserva_20509											AT%MX513.12: BOOL;
		(*01x20510*) Reserva_20510											AT%MX513.13:  BOOL;
		(*01x20511*) Reserva_20511											AT%MX513.14: BOOL;
		(*01x20512*) Reserva_20512											AT%MX513.15: BOOL;

		(*Turbina*)
		(*01x20513*) Turbina_DistribuidorFechado								AT%MX514.0: BOOL;
		(*01x20514*) Turbina_BorboletaAbrindo									AT%MX514.1: BOOL;
 		(*01x20515*) Turbina_BorboletaFechando								AT%MX514.2:  BOOL;
		(*01x20516*) Turbina_BorboletaCracking								AT%MX514.3:  BOOL;
		(*01x20517*) Turbina_BorboletaFechada								AT%MX514.4:  BOOL;
		(*01x20518*) Turbina_BorboletaAberta									AT%MX514.5:  BOOL;
		(*01x20519*) Turbina_BorboletaRetencao								AT%MX514.6:  BOOL;
		(*01x20520*) Turbina_BorboletaTravada								AT%MX514.7:  BOOL;
		(*01x20521*) Turbina_BorboletaDeriva									AT%MX514.8:  BOOL;
		(*01x20522*) Turbina_ByPassAbrindo									AT%MX514.9:  BOOL;
		(*01x20523*) Turbina_ByPassFechando								AT%MX514.10:  BOOL;
		(*01x20524*) Turbina_ByPassFechado									AT%MX514.11:  BOOL;
		(*01x20525*) Turbina_ByPassAberto									AT%MX514.12:  BOOL;
		(*01x20526*)Turbina_Operacional 										AT%MX514.13:  BOOL;
		(*01x20527*) Turbina_Equalizando										AT%MX514.14:  BOOL;
		(*01x20528*) Turbina_Equalizada										AT%MX514.15:  BOOL;
		(*01x20529*) Turbina_Aberta												AT%MX515.0: BOOL;
		(*01x20530*) Turbina_Fechada											AT%MX515.1: BOOL;
 		(*01x20531*) Turbina_PasDesalinhadas								AT%MX515.2:  BOOL;
		(*01x20532*) Turbina_Pressostato01 									AT%MX515.3:  BOOL;
		(*01x20533*) Turbina_Pressostato02									AT%MX515.4:  BOOL;
		(*01x20534*) Turbina_Pressostato03									AT%MX515.5:  BOOL;
		(*01x20535*) Reserva_20535											AT%MX515.6:  BOOL;
		(*01x20536*) Reserva_20536											AT%MX515.7:  BOOL;
		(*01x20537*) Reserva_20537 											AT%MX515.8:  BOOL;
		(*01x20538*) Reserva_20538 											AT%MX515.9:  BOOL;
		(*01x20539*) Reserva_20539 											AT%MX515.10:  BOOL;
		(*01x20540*) Reserva_20540											AT%MX515.11:  BOOL;
		(*01x20541*) Reserva_20541											AT%MX515.12:  BOOL;
		(*01x20542*) Reserva_20542											AT%MX515.13:  BOOL;
		(*01x20543*) Reserva_20543											AT%MX515.14:  BOOL;
		(*01x20544*) Reserva_20544											AT%MX515.15:  BOOL;

		(*Regulador de Velocidade*)
		(*01x20545*) RegV_Habilitado											AT%MX516.1: BOOL;
		(*01x20546*) RegV_Desabilitado 										AT%MX516.1: BOOL;
		(*01x20547*) RegV_ProtecoesAtuadas									AT%MX516.2: BOOL;
		(*01x20548*) RegV_TurbinaParada 										AT%MX516.3: BOOL;
		(*01x20549*) RegV_RPM030												AT%MX516.4: BOOL;
		(*01x20550*) RegV_RPM090												AT%MX516.5: BOOL;
		(*01x20551*) RegV_RPM100												AT%MX516.6:  BOOL;
		(*01x20552*) RegV_RPM125 											AT%MX516.7:  BOOL;
		(*01x20553*) RegV_CargaZerada										AT%MX516.8:  BOOL;
		(*01x20554*) RegV_ValvSeguranca01									AT%MX516.9:  BOOL;
		(*01x20555*) RegV_ValvSeguranca02									AT%MX516.10:  BOOL;
		(*01x20556*) RegV_ValvSeg_Borboleta 									AT%MX516.11:  BOOL;
		(*01x20557*) RegV_Ctrl_Man_Distribuidor_Status						AT%MX516.12:  BOOL;
		(*01x20558*) RegV_Ctrl_Man_ValvDistr_Status							AT%MX516.13:  BOOL;
		(*01x20559*) RegV_Ctrl_Man_Rotor_Status							AT%MX516.14:  BOOL;
		(*01x20560*) RegV_Ctrl_Velocidade_Status							AT%MX516.15:  BOOL;
		(*01x20561*) RegV_Estatismo_Status									AT%MX517.1: BOOL;
		(*01x20562*) RegV_BaseCarga_Status									AT%MX517.1: BOOL;
		(*01x20563*) RegV_Compensacao_PotP_Status	 					AT%MX517.2: BOOL;
		(*01x20564*) RegV_Ctrl_PotP_Status	 								AT%MX517.3: BOOL;
		(*01x20565*) RegV_MaquinaEmDescarga								AT%MX517.4: BOOL;
		(*01x20566*) Reserva_20566											AT%MX517.5: BOOL;
		(*01x20567*) Reserva_20567											AT%MX517.6:  BOOL;
		(*01x20568*) Reserva_20568 											AT%MX517.7:  BOOL;
		(*01x20569*) Reserva_20569											AT%MX517.8:  BOOL;
		(*01x20570*) Reserva_20570											AT%MX517.9:  BOOL;
		(*01x20571*) Reserva_20571											AT%MX517.10:  BOOL;
		(*01x20572*) Reserva_20572 											AT%MX517.11:  BOOL;
		(*01x20573*) Reserva_20573											AT%MX517.12:  BOOL;
		(*01x20574*) Reserva_20574											AT%MX517.13:  BOOL;
		(*01x20575*) Reserva_20575											AT%MX517.14:  BOOL;
		(*01x20576*) Reserva_20576											AT%MX517.15:  BOOL;

		(*Regulador de Tensão*)
		(*01x20577*) RegT_Habilitado 											AT%MX518.0:  BOOL;
		(*01x20578*) RegT_Desabilitado 										AT%MX518.1:  BOOL;
		(*01x20579*) RegT_41C_Ligado										AT%MX518.2:  BOOL;
		(*01x20580*) RegT_41C_Desligado 									AT%MX518.3: BOOL;
		(*01x20581*) RegT_PreExcitacao										AT%MX518.4: BOOL;
		(*01x20582*) RegT_SemErro											AT%MX518.5: BOOL;
		(*01x20583*) RegT_TensaoEstabilizada								AT%MX518.6: BOOL;
		(*01x20584*) RegT_Protecao_Atuada 									AT%MX518.7: BOOL;
		(*01x20585*) RegT_Ctrl_Tensao_Status								AT%MX518.8: BOOL;
		(*01x20586*) RegT_Ctrl_FP_Status										AT%MX518.9:  BOOL;
		(*01x20587*) RegT_Ctrl_VAR_Status									AT%MX518.10:  BOOL;
		(*01x20588*) RegT_Escova_Positiva									AT%MX518.11: BOOL;
		(*01x20589*) RegT_Escova_Negativa									AT%MX518.12: BOOL;
		(*01x20590*) Reserva_20590											AT%MX518.13: BOOL;
		(*01x20591*) Reserva_20591											AT%MX518.14:  BOOL;
		(*01x20592*) Reserva_20592											AT%MX518.15:  BOOL;
		(*01x20593*) Reserva_20593 											AT%MX519.0:  BOOL;
		(*01x20594*) Reserva_20594 											AT%MX519.1:  BOOL;
		(*01x20595*) Reserva_20595											AT%MX519.2:  BOOL;
		(*01x20596*) Reserva_20596 											AT%MX519.3: BOOL;
		(*01x20597*) Reserva_20597											AT%MX519.4: BOOL;
		(*01x20598*) Reserva_20598											AT%MX519.5: BOOL;
		(*01x20599*) Reserva_20599											AT%MX519.6: BOOL;
		(*01x20600*) Reserva_20600 											AT%MX519.7: BOOL;
		(*01x20601*) Reserva_20601											AT%MX519.8: BOOL;
		(*01x20602*) Reserva_20602											AT%MX519.9:  BOOL;
		(*01x20603*) Reserva_20603											AT%MX519.10:  BOOL;
		(*01x20604*) Reserva_20604											AT%MX519.11: BOOL;
		(*01x20605*) Reserva_20605 											AT%MX519.12: BOOL;
		(*01x20606*) Reserva_20606											AT%MX519.13: BOOL;
		(*01x20607*) Reserva_20607											AT%MX519.14:  BOOL;
		(*01x20608*) Reserva_20608											AT%MX519.15:  BOOL;

		(*Sincronismo*)
		(*01x20609*) Sinc_Habilitado											AT%MX520.0:  BOOL;
		(*01x20610*) Sinc_ModoAuto											AT%MX520.1:  BOOL;
		(*01x20611*) Sinc_ModoManual											AT%MX520.2:  BOOL;
		(*01x20612*) Sinc_ModoBM												AT%MX520.3:  BOOL;
		(*01x20613*) Reserva_20613											AT%MX520.4: BOOL;
		(*01x20614*) Reserva_20614											AT%MX520.5: BOOL;
		(*01x20615*) Reserva_20615											AT%MX520.6: BOOL;
		(*01x20616*) Reserva_20616 											AT%MX520.7: BOOL;
		(*01x20617*) Reserva_20617											AT%MX520.8: BOOL;
		(*01x20618*) Reserva_20618											AT%MX520.9:  BOOL;
		(*01x20619*) Reserva_20619											AT%MX520.10:  BOOL;
		(*01x20620*) Reserva_20620											AT%MX520.11: BOOL;
		(*01x20621*) Reserva_20621 											AT%MX520.12: BOOL;
		(*01x20622*) Reserva_20622											AT%MX520.13: BOOL;
		(*01x20623*) Reserva_20623											AT%MX520.14:  BOOL;
		(*01x20624*) Reserva_20624											AT%MX520.15:  BOOL;

		(*Relésde Bloqueio*)
		(*01x20625*) Rele86E_Status											AT%MX521.0:  BOOL;
		(*01x20626*) Rele86M_Status											AT%MX521.1:  BOOL;
		(*01x20627*) Rele86H_Status											AT%MX521.2:  BOOL;
		(*01x20628*) Reserva_20628											AT%MX521.3:  BOOL;
		(*01x20629*) Reserva_20629											AT%MX521.4:  BOOL;
		(*01x20630*) Reserva_20630											AT%MX521.5:  BOOL;
		(*01x20631*) Reserva_20631											AT%MX521.6:  BOOL;
		(*01x20632*) Reserva_20632											AT%MX521.7:  BOOL;
		(*01x20633*) Reserva_20633											AT%MX521.8:  BOOL;
		(*01x20634*) Reserva_20634											AT%MX521.9:  BOOL;
		(*01x20635*) Reserva_20635											AT%MX521.10:  BOOL;
		(*01x20636*) Reserva_20636											AT%MX521.11:  BOOL;
		(*01x20637*) Reserva_20637											AT%MX521.12:  BOOL;
		(*01x20638*) Reserva_20638											AT%MX521.13:  BOOL;
		(*01x20639*) Reserva_20639											AT%MX521.14:  BOOL;
		(*01x20640*) Reserva_20640											AT%MX521.15:  BOOL;

		(*Analógicas*)

		(*Disjuntor 52G*)
		(*01x20641*) Disj52G_Aberto 											AT%MX522.0:  BOOL;
		(*01x20642*) Disj52G_Fechado											AT%MX522.1:  BOOL;
		(*01x20643*) Disj52G_Inconsistente									AT%MX522.2:  BOOL;
		(*01x20644*) Disj52G_MolaCarregada									AT%MX522.3:  BOOL;
		(*01x20645*) Disj52G_ModoTeste										AT%MX522.4:  BOOL;
		(*01x20646*) Disj52G_Inserido											AT%MX522.5:  BOOL;
		(*01x20647*) Disj52G_Extraido 											AT%MX522.6:  BOOL;
		(*01x20648*) Disj52L_Aberto											AT%MX522.7:  BOOL;
		(*01x20649*) Disj52L_Fechado											AT%MX522.8:  BOOL;
		(*01x20650*) Reserva_20650											AT%MX522.9:  BOOL;
		(*01x20651*) Reserva_20651											AT%MX522.10:  BOOL;
		(*01x20652*) Reserva_20652											AT%MX522.11:  BOOL;
		(*01x20653*) Reserva_20653 											AT%MX522.12:  BOOL;
		(*01x20654*) Reserva_20654											AT%MX522.13:  BOOL;
		(*01x20655*) Reserva_20655											AT%MX522.14:  BOOL;
		(*01x20656*) Reserva_20656											AT%MX522.15:  BOOL;

		(*Disjuntores Auxilares*)
		(*01x20657*) PCP_DisjQCCV_Status									AT%MX523.0:  BOOL;
		(*01x20658*) PCP_DisjQCAG_Status									AT%MX523.1:  BOOL;
		(*01x20659*) PCP_DisjQCAR_Status									AT%MX523.2:  BOOL;
		(*01x20660*) CS_DisjQCC_Status										AT%MX523.3:  BOOL;
		(*01x20661*) CS_DisjQCA01_Status									AT%MX523.4:  BOOL;
		(*01x20662*) CS_DisjQCA02_Status									AT%MX523.5:  BOOL;
		(*01x20663*) Reserva_20663											AT%MX523.6:  BOOL;
		(*01x20664*) Reserva_20664											AT%MX523.7:  BOOL;
		(*01x20665*) Reserva_20665											AT%MX523.8:  BOOL;
		(*01x20666*) Reserva_20666											AT%MX523.9:  BOOL;
		(*01x20667*) Reserva_20667											AT%MX523.10:  BOOL;
		(*01x20668*) Reserva_20668											AT%MX523.11:  BOOL;
		(*01x20669*) Reserva_20669											AT%MX523.12:  BOOL;
		(*01x20670*) Reserva_20670											AT%MX523.13:  BOOL;
		(*01x20671*) Reserva_20671											AT%MX523.14:  BOOL;
		(*01x20672*) Reserva_20672											AT%MX523.15:  BOOL;

		(*Vibracao*)

		(*Relé de Proteção*)
		(*01x20673*) F50_Atuado												AT%MX524.0:  BOOL;
		(*01x20674*) Reserva_20674											AT%MX524.1:  BOOL;
		(*01x20675*) Reserva_20675											AT%MX524.2:  BOOL;
		(*01x20676*) Reserva_20676											AT%MX524.3:  BOOL;
		(*01x20677*) Reserva_20677											AT%MX524.4:  BOOL;
		(*01x20678*) Reserva_20678											AT%MX524.5:  BOOL;
		(*01x20679*) Reserva_20679											AT%MX524.6:  BOOL;
		(*01x20680*) Reserva_20680											AT%MX524.7:  BOOL;
		(*01x20681*) Reserva_20681											AT%MX524.8:  BOOL;
		(*01x20682*) Reserva_20682											AT%MX524.9:  BOOL;
		(*01x20683*) Reserva_20683											AT%MX524.10:  BOOL;
		(*01x20684*) Reserva_20684											AT%MX524.11:  BOOL;
		(*01x20685*) Reserva_20685											AT%MX524.12:  BOOL;
		(*01x20686*) Reserva_20686											AT%MX524.13:  BOOL;
		(*01x20687*) Reserva_20687											AT%MX524.14:  BOOL;
		(*01x20688*) Reserva_20688											AT%MX524.15:  BOOL;
		(*01x20689*) Reserva_20689											AT%MX525.0:  BOOL;
		(*01x20690*) Reserva_20690											AT%MX525.1:  BOOL;
		(*01x20691*) Reserva_20691											AT%MX525.2:  BOOL;
		(*01x20692*) Reserva_20692											AT%MX525.3:  BOOL;
		(*01x20693*) Reserva_20693											AT%MX525.4:  BOOL;
		(*01x20694*) Reserva_20694											AT%MX525.5:  BOOL;
		(*01x20695*) Reserva_20695											AT%MX525.6:  BOOL;
		(*01x20696*) Reserva_20696											AT%MX525.7:  BOOL;
		(*01x20697*) Reserva_20697											AT%MX525.8:  BOOL;
		(*01x20698*) Reserva_20698											AT%MX525.9:  BOOL;
		(*01x20699*) Reserva_20699											AT%MX525.10:  BOOL;
		(*01x20700*) Reserva_20700											AT%MX525.11:  BOOL;
		(*01x20701*) Reserva_20701											AT%MX525.12:  BOOL;
		(*01x20702*) Reserva_20702											AT%MX525.13:  BOOL;
		(*01x20703*) Reserva_20703											AT%MX525.14:  BOOL;
		(*01x20704*) Reserva_20704											AT%MX525.15:  BOOL;

		(*Reset Alarmes*)
		(*01x20705*) AlarmeAtivo													AT%MX526.0:  BOOL;
		(*01x20706*) AlarmeLatente												AT%MX526.1:  BOOL;
		(*01x20707*) Reserva_20707											AT%MX526.2:  BOOL;
		(*01x20708*) Reserva_20708											AT%MX526.3:  BOOL;
		(*01x20709*) Reserva_20709											AT%MX526.4:  BOOL;
		(*01x20710*) Reserva_20710											AT%MX526.5:  BOOL;
		(*01x20711*) Reserva_20711											AT%MX526.6:  BOOL;
		(*01x20712*) Reserva_20712											AT%MX526.7:  BOOL;
		(*01x20713*) Reserva_20713											AT%MX526.8:  BOOL;
		(*01x20714*) Reserva_20714											AT%MX526.9:  BOOL;
		(*01x20715*) Reserva_20715											AT%MX526.10:  BOOL;
		(*01x20716*) Reserva_20716											AT%MX526.11:  BOOL;
		(*01x20717*) Reserva_20717											AT%MX526.12:  BOOL;
		(*01x20718*) Reserva_20718											AT%MX526.13:  BOOL;
		(*01x20719*) Reserva_20719											AT%MX526.14:  BOOL;
		(*01x20720*) Reserva_20720											AT%MX526.15:  BOOL;

		(*Totalizador de Potência*)

		(*Temperaturas*)

		(*Monitor Barragem*)

		(*Horímetro*)

		(*Mapa Lógico*)
		(*01x20721*) QTA_Emergencia_Remota								AT%MX527.0: BOOL;
		(*01x20722*) QTA_Comporta_Fechada									AT%MX527.1: BOOL;
		(*01x20723*) QTA_Comporta_Aberta									AT%MX527.2: BOOL;
		(*01x20724*) QTA_Comporta_Abrindo									AT%MX527.3: BOOL;
		(*01x20725*) QTA_Comporta_Fechando								AT%MX527.4: BOOL;
		(*01x20726*) QTA_Comporta_Cracking									AT%MX527.5: BOOL;
		(*01x20727*) QTA_Comporta_Reposicao								AT%MX527.6:  BOOL;
		(*01x20728*) QTA_ComportaTravadaTimeOut							AT%MX527.7:  BOOL;
		(*01x20729*) QTA_Bomba01_Ligada									AT%MX527.8:  BOOL;
		(*01x20730*) QTA_Bomba01_TRIP										AT%MX527.9:  BOOL;
		(*01x20731*) QTA_Bomba02_Ligada 									AT%MX527.10:  BOOL;
		(*01x20732*) QTA_Bomba02_TRIP										AT%MX527.11:  BOOL;
		(*01x20733*) QTA_Falha_Comunicacao									AT%MX527.12:  BOOL;
		(*01x20734*) QTA_Bomba03_Ligada 									AT%MX527.13:  BOOL;
		(*01x20735*) QTA_Bomba03_TRIP										AT%MX527.14:  BOOL;
		(*01x20736*) Reserva_20736											AT%MX527.15:  BOOL;

		(*01x20737*) Reserva_20737											AT%MX528.0: BOOL;
		(*01x20738*) Reserva_20738											AT%MX528.1: BOOL;
		(*01x20739*) Reserva_20739											AT%MX528.2: BOOL;
		(*01x20740*) Reserva_20740											AT%MX528.3: BOOL;
		(*01x20741*) Reserva_20741											AT%MX528.4: BOOL;
		(*01x20742*) Reserva_20742											AT%MX528.5: BOOL;
		(*01x20743*) Reserva_20743											AT%MX528.6:  BOOL;
		(*01x20744*) Reserva_20744											AT%MX528.7:  BOOL;
		(*01x20745*) Reserva_20745											AT%MX528.8:  BOOL;
		(*01x20746*) Reserva_20746											AT%MX528.9:  BOOL;
		(*01x20747*) Reserva_20747 											AT%MX528.10:  BOOL;
		(*01x20748*) Reserva_20748											AT%MX528.11:  BOOL;
		(*01x20749*) Reserva_20749											AT%MX528.12:  BOOL;
		(*01x20750*) Reserva_20750 											AT%MX528.13:  BOOL;
		(*01x20751*) Reserva_20751											AT%MX528.14:  BOOL;
		(*01x20752*) Reserva_20752											AT%MX528.15:  BOOL;

		(*01x20753*) PSA_Emergencia											AT%MX529.0: BOOL;
		(*01x20754*) PSA_NivelEmergenciaPoco								AT%MX529.1: BOOL;
		(*01x20755*) PSA_Falha_Comunicacao								AT%MX529.2: BOOL;
		(*01x20756*) PSA_MonitorBarragemLL									AT%MX529.3: BOOL;
		(*01x20757*) Reserva_20757											AT%MX529.4: BOOL;
		(*01x20758*) Reserva_20758											AT%MX529.5: BOOL;
		(*01x20759*) Reserva_20759											AT%MX529.6:  BOOL;
		(*01x20760*) Reserva_20760											AT%MX529.7:  BOOL;
		(*01x20761*) Reserva_20761											AT%MX529.8:  BOOL;
		(*01x20762*) Reserva_20762											AT%MX529.9:  BOOL;
		(*01x20763*) Reserva_20763 											AT%MX529.10:  BOOL;
		(*01x20764*) Reserva_20764											AT%MX529.11:  BOOL;
		(*01x20765*) Reserva_20765											AT%MX529.12:  BOOL;
		(*01x20766*) Reserva_20766 											AT%MX529.13:  BOOL;
		(*01x20767*) Reserva_20767											AT%MX529.14:  BOOL;
		(*01x20768*) Reserva_20768											AT%MX529.15:  BOOL;
'''

leituras = '''

	(*UHLM*)
	(*04x13289*) UHLM_PressaoOleo											AT%MW1000: INT;
	(*04x13290*) UHLM_VazaoOleo												AT%MW1001: INT;
	(*04x13291*) Reserva_13291												AT%MW1002: INT;
	(*04x13292*) Reserva_13292												AT%MW1003: INT;
	(*04x13293*) Reserva_13293												AT%MW1004: INT;
	(*04x13294*) Reserva_13294												AT%MW1005: INT;

	(*UHRV*)
	(*04x13295*) UHRV_PressaoOleo											AT%MW1006: INT;
	(*04x13296*) Reserva_13296												AT%MW1007: INT;
	(*04x13297*) Reserva_13297												AT%MW1008: INT;
	(*04x13298*) Reserva_13298												AT%MW1009: INT;
	(*04x13299*) Reserva_13299												AT%MW1010: INT;
	(*04x13300*) Reserva_13300												AT%MW1011: INT;

	(*Turbinna*)
	(*04x13301*) Turbina_JusanteBorboleta									AT%MW1012: INT;
	(*04x13302*) Turbina_MontanteBorboleta									AT%MW1013: INT;
	(*04x13303*) Turbina_PosicaoDistribuidor									AT%MW1014: REAL;
	(*04x13305*) Turbina_PosicaoRotor											AT%MW1016: REAL;
	(*04x13307*) Turbina_Velocidade											AT%MW1018: INT;
	(*04x13308*) Turbina_Vazao													AT%MW1019: INT;
	(*04x13309*) Turbina_Tempo_AberturaBorboleta							AT%MW1020: DINT;
	(*04x13311*) Turbina_Tempo_AberturaBorboleta_Minuto					AT%MW1022: TIME;
	(*04x13313*) Turbina_Tempo_FechamentoBorboleta						AT%MW1024: DINT;
	(*04x13315*) Turbina_Tempo_FechamentoBorboleta_Minuto				AT%MW1026: TIME;
	(*04x13317*) Turbina_Tempo_AberturaByPass								AT%MW1028: DINT;
	(*04x13319*) Turbina_Tempo_AberturaByPass_Minuto					AT%MW1030: TIME;
	(*04x13321*) Turbina_Tempo_FechamentoByPass						AT%MW1032: DINT;
	(*04x13323*) Turbina_Tempo_FechamentoByPass_Minuto				AT%MW1034: TIME;
	(*04x13325*) Turbina_TempoEqualizacao	 								AT%MW1036: DINT;
	(*04x13327*) Turbina_TempoEqualizacao_Minuto							AT%MW1038: TIME;
	(*04x13329*) Turbina_Vibracao01											AT%MW1040: INT;
	(*04x13330*) Turbina_Vibracao02											AT%MW1041: INT;
	(*04x13331*) Turbina_Vibracao03											AT%MW1042: INT;
	(*04x13332*) Turbina_Vibracao04											AT%MW1043: INT;
	(*04x13333*) Turbina_Vibracao05											AT%MW1044: INT;
	(*04x13334*) Turbina_Vibracao06											AT%MW1045: INT;
	(*04x13335*) Turbina_Vibracao07											AT%MW1046: INT;
	(*04x13336*) Turbina_Vibracao08											AT%MW1047: INT;
	(*04x13337*) Turbina_Vibracao09											AT%MW1048: INT;
	(*04x13338*) Turbina_Vibracao10											AT%MW1049: INT;
	(*04x13339*) Reserva_13337												AT%MW1050: INT;
	(*04x13340*) Reserva_13338												AT%MW1051: INT;
	(*04x13341*) Reserva_13339												AT%MW1052: INT;
	(*04x13342*) Reserva_13340												AT%MW1053: INT;
	(*04x13343*) Reserva_13341												AT%MW1054: INT;
	(*04x13344*) Reserva_13342												AT%MW1055: INT;
	(*04x13345*) Reserva_13343												AT%MW1056: INT;
	(*04x13346*) Reserva_13344												AT%MW1057: INT;
	(*04x13347*) Reserva_13345												AT%MW1058: INT;
	(*04x13348*) Reserva_13346												AT%MW1059: INT;

	(*Gerador*)
	(*04x13349*)	F50_U_FaseAB												AT%MW1060: INT;
	(*04x13350*)	F50_U_FaseBC												AT%MW1061: INT;
	(*04x13351*)	F50_U_FaseCA												AT%MW1062: INT;
	(*04x13352*)	F50_U_Neutro												AT%MW1063: INT;
	(*04x13353*)	F50_U_FaseAN												AT%MW1064: INT;
	(*04x13354*)	F50_U_FaseBN												AT%MW1065: INT;
	(*04x13355*)	F50_U_FaseCN												AT%MW1066: INT;
	(*04x13356*)	F50_I_FaseA													AT%MW1067: INT;
	(*04x13357*)	F50_I_FaseB													AT%MW1068: INT;
	(*04x13358*)	F50_I_FaseC													AT%MW1069: INT;
	(*04x13359*)	F50_I_Neutro													AT%MW1070: INT;
	(*04x13360*)	F50_P_INST													AT%MW1071: INT;
	(*04x13361*)	F50_Q_INST													AT%MW1072: INT;
	(*04x13362*)	F50_S_INST													AT%MW1073: INT;
	(*04x13363*)	F50_PF_INST													AT%MW1074: INT;
	(*04x13364*)	F50_FHz_INST												AT%MW1075: INT;
	(*04x13365*)	F50_U_SeqPos												AT%MW1076: INT;
	(*04x13366*)	F50_U_SeqNeg												AT%MW1077: INT;
	(*04x13367*)	F50_U_SeqZero												AT%MW1078: INT;
	(*04x13368*)	F50_I_SeqPos												AT%MW1079: INT;
	(*04x13369*)	F50_I_SeqNeg												AT%MW1080: INT;
	(*04x13370*)	F50_I_SeqZero												AT%MW1081: INT;
	(*04x13371*)	Reserva_13369												AT%MW1082: INT;
	(*04x13372*)	Reserva_13370												AT%MW1083: INT;
	(*04x13373*)	Reserva_13371												AT%MW1084: INT;
	(*04x13374*)	Reserva_13372												AT%MW1085: INT;
	(*04x13375*)	Reserva_13373												AT%MW1086: INT;
	(*04x13376*)	Reserva_13374												AT%MW1087: INT;
	(*04x13377*)	Reserva_13375												AT%MW1088: INT;
	(*04x13378*)	Reserva_13376												AT%MW1089: INT;
	(*04x13379*)	Gerador_Vbarra												AT%MW1090: INT;
	(*04x13380*)	Gerador_ExcitacaoTensao									AT%MW1091: INT;
	(*04x13381*)	Gerador_ExcitacaoCorrente									AT%MW1092: INT;

	(*04x13407*)	Gerador_Media_Varm										AT%MW1118: INT;
	(*04x13408*)	Gerador_Media_Iarm											AT%MW1119: INT;

	(*Temperaturas*)
	(*04x13409*) 	MED_750450_AR1_RTD1   									AT%MW1120: REAL;
	(*04x13411*)	MED_750450_AR1_RTD2									AT%MW1122: REAL;
	(*04x13413*)	MED_750450_AR1_RTD3									AT%MW1124: REAL;
	(*04x13415*)	MED_750450_AR1_RTD4 									AT%MW1126: REAL;
	(*04x13417*)	MED_750450_AR2_RTD1									AT%MW1128: REAL;
	(*04x13419*)	MED_750450_AR2_RTD2									AT%MW1130: REAL;
	(*04x13421*)	MED_750450_AR2_RTD3									AT%MW1132: REAL;
	(*04x13423*)	MED_750450_AR2_RTD4									AT%MW1134: REAL;
	(*04x13425*)	MED_750450_AR3_RTD1									AT%MW1136: REAL;
	(*04x13427*)	MED_750450_AR3_RTD2									AT%MW1138: REAL;
	(*04x13429*)	MED_750450_AR3_RTD3									AT%MW1140: REAL;
	(*04x13431*)	MED_750450_AR3_RTD4									AT%MW1142: REAL;
	(*04x13433*)	MED_750450_AR4_RTD1									AT%MW1144: REAL;
	(*04x13435*)	MED_750450_AR4_RTD2									AT%MW1146: REAL;
	(*04x13437*)	MED_750450_AR4_RTD3									AT%MW1148: REAL;
	(*04x13439*)	MED_750450_AR4_RTD4									AT%MW1150: REAL;
	(*04x13441*) 	MED_750450_AR5_RTD1   									AT%MW1152: REAL;
	(*04x13443*)	MED_750450_AR5_RTD2									AT%MW1154: REAL;
	(*04x13445*)	MED_750450_AR5_RTD3									AT%MW1156: REAL;
	(*04x13447*)	MED_750450_AR5_RTD4 									AT%MW1158: REAL;
	(*04x13449*)	MED_750450_AR6_RTD1									AT%MW1160: REAL;
	(*04x13451*)	MED_750450_AR6_RTD2									AT%MW1162: REAL;
	(*04x13453*)	MED_750450_AR6_RTD3									AT%MW1164: REAL;
	(*04x13455*)	MED_750450_AR6_RTD4									AT%MW1166: REAL;
	(*04x13457*)	MED_750450_AR7_RTD1									AT%MW1168: REAL;
	(*04x13459*)	MED_750450_AR7_RTD2									AT%MW1170: REAL;
	(*04x13461*)	MED_750450_AR7_RTD3									AT%MW1172: REAL;
	(*04x13463*)	MED_750450_AR7_RTD4									AT%MW1174: REAL;
	(*04x13465*)	MED_750450_AR8_RTD1									AT%MW1176: REAL;
	(*04x13467*)	MED_750450_AR8_RTD2									AT%MW1178: REAL;
	(*04x13469*)	MED_750450_AR8_RTD3									AT%MW1180: REAL;
	(*04x13471*)	MED_750450_AR8_RTD4									AT%MW1182: REAL;

	(*Monitor Barragem*)
	(*04x13473*) QCC_NivelMontante_Grade									AT%MW1184: INT;
	(*04x13474*) QCC_NivelJusante_Grade									AT%MW1185: INT;
	(*04x13475*) QTA_NivelJusante_CanalFuga								AT%MW1186: INT;
	(*04x13476*) QTA_NivelMontante_Grade									AT%MW1187: INT;
	(*04x13477*) QTA_NivelJusante_Grade										AT%MW1188: INT;
'''
setpoints = '''
	(*UHLM*)
	(*04x13789*)	Setpoint_UHLM_Pressao_Maxima	AT%MW1500: INT;
	(*04x13790*)	Setpoint_UHLM_Pressao_Minima	AT%MW1501: INT;
	(*04x13791*)	Setpoint_UHLM_Pressao_Alarme	AT%MW1502: INT;
	(*04x13792*)	Setpoint_UHLM_Pressao_TRIP		AT%MW1503: INT;
	(*04x13793*)	Setpoint_UHLM_Temp_Alarme		AT%MW1504: REAL;
	(*04x13795*)	Setpoint_UHLM_Temp_TRIP			AT%MW1506: REAL;
	(*04x13797*)	Setpoint_UHLM_Temp_ResAquec	AT%MW1508: REAL;
	(*04x13799*)	Setpoint_UHLM_Vazao_Oleo			AT%MW1510: REAL;
	(*04x13801*)	Setpoint_UHLM_Temp_Oleo			AT%MW1512: REAL;
	(*04x13803*)	Setpoint_UHLM_Temp_TrocCalor	AT%MW1514: REAL;

	(*UHRV*)
	(*04x13805*) Setpoint_UHRV_Pressao_Maxima	AT%MW1516: INT;
	(*04x13806*) Setpoint_UHRV_Pressao_Minima	AT%MW1517: INT;
	(*04x13807*) Setpoint_UHRV_Pressao_Alarme	AT%MW1518: INT;
	(*04x13808*) Setpoint_UHRV_Pressao_TRIP		AT%MW1519: INT;
	(*04x13809*) Setpoint_UHRV_Temp_Alarme		AT%MW1520: REAL;
	(*04x13811*) Setpoint_UHRV_Temp_TRIP			AT%MW1522: REAL;
	(*04x13813*)Setpoint_UHRV_Temp_ResAquec	AT%MW1524: REAL;

	(*Turbina*)
	(*04x13815*) Setpoit_Turb_Sobrevelocidade		AT%MW1526: INT;
	(*04x13817*) Setpoit_Turb_PressaoMinima			AT%MW1528: REAL;
	(*04x13819*) Setpoit_Turb_TempoEqualizacao		AT%MW1530: REAL;
	(*04x13821*) Setpoint_Vibracao01_Trip   			AT%MW1532: REAL;
	(*04x13823*) Setpoint_Vibracao02_Trip				AT%MW1534: REAL;
	(*04x13825*) Setpoint_Vibracao03_Trip				AT%MW1536: REAL;
	(*04x13827*) Setpoint_Vibracao04_Trip				AT%MW1538: REAL;
	(*04x13829*) Setpoint_Vibracao05_Trip				AT%MW1540: REAL;
	(*04x13831*) Setpoint_Vibracao06_Trip   			AT%MW1542: REAL;
	(*04x13833*) Setpoint_Vibracao07_Trip				AT%MW1544: REAL;
	(*04x13835*) Setpoint_Vibracao08_Trip				AT%MW1546: REAL;
	(*04x13837*) Setpoint_Vibracao09_Trip				AT%MW1548: REAL;
	(*04x13839*) Setpoint_Vibracao10_Trip				AT%MW1550: REAL;
	(*04x13841*) Setpoint_Vibracao01_Alarme   		AT%MW1552: REAL;
	(*04x13843*) Setpoint_Vibracao02_Alarme  		AT%MW1554: REAL;
	(*04x13845*) Setpoint_Vibracao03_Alarme  		AT%MW1556: REAL;
	(*04x13847*) Setpoint_Vibracao04_Alarme  		AT%MW1558: REAL;
	(*04x13849*) Setpoint_Vibracao05_Alarme  		AT%MW1560: REAL;
	(*04x13851*) Setpoint_Vibracao06_Alarme     		AT%MW1562: REAL;
	(*04x13853*) Setpoint_Vibracao07_Alarme  		AT%MW1564: REAL;
	(*04x13855*) Setpoint_Vibracao08_Alarme  		AT%MW1566: REAL;
	(*04x13857*) Setpoint_Vibracao09_Alarme  		AT%MW1568: REAL;
	(*04x13859*) Setpoint_Vibracao10_Alarme  		AT%MW1570: REAL;
	(*04x13861*) Reserva_13861				  		AT%MW1572: REAL;
	(*04x13863*) Reserva_13863     						AT%MW1574: REAL;
	(*04x13865*) Reserva_13865  						AT%MW1576: REAL;
	(*04x13867*) Reserva_13867  						AT%MW1578: REAL;
	(*04x13869*) Reserva_13869  						AT%MW1580: REAL;
	(*04x13871*) Reserva_13871  						AT%MW1582: REAL;

	(*Controle de Potência*)
	(*04x13873*)	CtrlP_PotenciaSetpoint				AT%MW1584: INT;
	(*04x13874*)	CtrlP_PotenciaMaxima				AT%MW1585: INT;
	(*04x13875*)	CtrlP_PotenciaMinima				AT%MW1586: INT;
	(*04x13877*)	CtrlP_NivelSetpoint					AT%MW1588: REAL;
	(*04x13879*)	CtrlP_NivelDesligamento				AT%MW1590: REAL;
	(*04x13881*)	CtrlP_NivelReligamento				AT%MW1592: REAL;
	(*04x13883*)	CtrlP_NivelGanho						AT%MW1594: INT;
	(*04x13884*)	CtrlP_NivelIntervalo					AT%MW1595: INT;
	(*04x13885*)	CtrlP_NivelTolerancia					AT%MW1596: INT;
	(*04x13887*)	CtrlP_NivelAlarme					AT%MW1598: REAL;
	(*04x13889*)	CtrlP_NivelTrip						AT%MW1600: REAL;
	(*04x13891*)	CtrlQ_SetpointFP						AT%MW1602: INT;
	(*04x13892*)	CtrlQ_SetpointkVAr					AT%MW1603: INT;
	(*04x13893*)	Reserva_13893						AT%MW1604: INT;
	(*04x13894*)	GRTD_PotenciaSetpoint						AT%MW1605: REAL;

	(*Temperaturas*)
	(*04x13897*)	Setpoint_AR1_RTD1_TRIP				AT%MW1608: REAL;
	(*04x13899*)	Setpoint_AR1_RTD2_TRIP				AT%MW1610: REAL;
	(*04x13901*)	Setpoint_AR1_RTD3_TRIP				AT%MW1612: REAL;
	(*04x13903*)	Setpoint_AR1_RTD4_TRIP				AT%MW1614: REAL;
	(*04x13905*)	Setpoint_AR2_RTD1_TRIP				AT%MW1616: REAL;
	(*04x13907*)	Setpoint_AR2_RTD2_TRIP				AT%MW1618: REAL;
	(*04x13909*)	Setpoint_AR2_RTD3_TRIP				AT%MW1620: REAL;
	(*04x13911*)	Setpoint_AR2_RTD4_TRIP				AT%MW1622: REAL;
	(*04x13913*)	Setpoint_AR3_RTD1_TRIP				AT%MW1624: REAL;
	(*04x13915*)	Setpoint_AR3_RTD2_TRIP				AT%MW1626: REAL;
	(*04x13917*)	Setpoint_AR3_RTD3_TRIP				AT%MW1628: REAL;
	(*04x13919*)	Setpoint_AR3_RTD4_TRIP				AT%MW1630: REAL;
 	(*04x13921*)	Setpoint_AR4_RTD1_TRIP				AT%MW1632: REAL;
	(*04x13923*)	Setpoint_AR4_RTD2_TRIP				AT%MW1634: REAL;
	(*04x13925*)	Setpoint_AR4_RTD3_TRIP				AT%MW1636: REAL;
	(*04x13927*)	Setpoint_AR4_RTD4_TRIP				AT%MW1638: REAL;
 	(*04x13929*)	Setpoint_AR5_RTD1_TRIP				AT%MW1640: REAL;
	(*04x13931*)	Setpoint_AR5_RTD2_TRIP				AT%MW1642: REAL;
	(*04x13933*)	Setpoint_AR5_RTD3_TRIP				AT%MW1644: REAL;
	(*04x13935*)	Setpoint_AR5_RTD4_TRIP				AT%MW1646: REAL;
 	(*04x13937*)	Setpoint_AR6_RTD1_TRIP				AT%MW1648: REAL;
	(*04x13939*)	Setpoint_AR6_RTD2_TRIP				AT%MW1650: REAL;
	(*04x13941*)	Setpoint_AR6_RTD3_TRIP				AT%MW1652: REAL;
	(*04x13943*)	Setpoint_AR6_RTD4_TRIP				AT%MW1654: REAL;
 	(*04x13945*)	Setpoint_AR7_RTD1_TRIP				AT%MW1656: REAL;
	(*04x13947*)	Setpoint_AR7_RTD2_TRIP				AT%MW1658: REAL;
	(*04x13949*)	Setpoint_AR7_RTD3_TRIP				AT%MW1660: REAL;
	(*04x13951*)	Setpoint_AR7_RTD4_TRIP				AT%MW1662: REAL;
 	(*04x13953*)	Setpoint_AR8_RTD1_TRIP				AT%MW1664: REAL;
	(*04x13955*)	Setpoint_AR8_RTD2_TRIP				AT%MW1666: REAL;
	(*04x13957*)	Setpoint_AR8_RTD3_TRIP				AT%MW1668: REAL;
	(*04x13959*)	Setpoint_AR8_RTD4_TRIP				AT%MW1670: REAL;
	(*04x13961*)	Setpoint_AR1_RTD1_Alarme			AT%MW1672: REAL;
	(*04x13963*)	Setpoint_AR1_RTD2_Alarme			AT%MW1674: REAL;
	(*04x13965*)	Setpoint_AR1_RTD3_Alarme			AT%MW1676: REAL;
	(*04x13967*)	Setpoint_AR1_RTD4_Alarme			AT%MW1678: REAL;
	(*04x13969*)	Setpoint_AR2_RTD1_Alarme			AT%MW1680: REAL;
	(*04x13971*)	Setpoint_AR2_RTD2_Alarme			AT%MW1682: REAL;
	(*04x13973*)	Setpoint_AR2_RTD3_Alarme			AT%MW1684: REAL;
	(*04x13975*)	Setpoint_AR2_RTD4_Alarme			AT%MW1686: REAL;
	(*04x13977*)	Setpoint_AR3_RTD1_Alarme			AT%MW1688: REAL;
	(*04x13979*)	Setpoint_AR3_RTD2_Alarme			AT%MW1690: REAL;
	(*04x13981*)	Setpoint_AR3_RTD3_Alarme			AT%MW1692: REAL;
	(*04x13983*)	Setpoint_AR3_RTD4_Alarme			AT%MW1694: REAL;
 	(*04x13985*)	Setpoint_AR4_RTD1_Alarme			AT%MW1696: REAL;
	(*04x13987*)	Setpoint_AR4_RTD2_Alarme			AT%MW1698: REAL;
	(*04x13989*)	Setpoint_AR4_RTD3_Alarme			AT%MW1700: REAL;
	(*04x13991*)	Setpoint_AR4_RTD4_Alarme			AT%MW1702: REAL;
 	(*04x13993*)	Setpoint_AR5_RTD1_Alarme			AT%MW1704: REAL;
	(*04x13995*)	Setpoint_AR5_RTD2_Alarme			AT%MW1706: REAL;
	(*04x13997*)	Setpoint_AR5_RTD3_Alarme			AT%MW1708: REAL;
	(*04x13999*)	Setpoint_AR5_RTD4_Alarme			AT%MW1710: REAL;
 	(*04x14001*)	Setpoint_AR6_RTD1_Alarme			AT%MW1712: REAL;
	(*04x14003*)	Setpoint_AR6_RTD2_Alarme			AT%MW1714: REAL;
	(*04x14005*)	Setpoint_AR6_RTD3_Alarme			AT%MW1716: REAL;
	(*04x14007*)	Setpoint_AR6_RTD4_Alarme			AT%MW1718: REAL;
	(*04x14009*)	Setpoint_AR7_RTD1_Alarme			AT%MW1720: REAL;
 	(*04x14011*)	Setpoint_AR7_RTD2_Alarme			AT%MW1722: REAL;
	(*04x14013*)	Setpoint_AR7_RTD3_Alarme			AT%MW1724: REAL;
	(*04x14015*)	Setpoint_AR7_RTD4_Alarme			AT%MW1726: REAL;
	(*04x14017*)	Setpoint_AR8_RTD1_Alarme			AT%MW1728: REAL;
	(*04x14019*)	Setpoint_AR8_RTD2_Alarme			AT%MW1730: REAL;
 	(*04x14021*)	Setpoint_AR8_RTD3_Alarme			AT%MW1732: REAL;
 	(*04x14023*)	Setpoint_AR8_RTD4_Alarme			AT%MW1734: REAL;
	(*04x14025*)	Setpoint_AR1_RTD1_PickupProtecao	AT%MW1736: REAL;
	(*04x14027*)	Setpoint_AR1_RTD2_PickupProtecao	AT%MW1738: REAL;
	(*04x14029*)	Setpoint_AR1_RTD3_PickupProtecao	AT%MW1740: REAL;
	(*04x14031*)	Setpoint_AR1_RTD4_PickupProtecao	AT%MW1742: REAL;
	(*04x14033*)	Setpoint_AR2_RTD1_PickupProtecao	AT%MW1744: REAL;
	(*04x14035*)	Setpoint_AR2_RTD2_PickupProtecao	AT%MW1746: REAL;
	(*04x14037*)	Setpoint_AR2_RTD3_PickupProtecao	AT%MW1748: REAL;
	(*04x14039*)	Setpoint_AR2_RTD4_PickupProtecao	AT%MW1750: REAL;
	(*04x14041*)	Setpoint_AR3_RTD1_PickupProtecao	AT%MW1752: REAL;
	(*04x14043*)	Setpoint_AR3_RTD2_PickupProtecao	AT%MW1754: REAL;
	(*04x14045*)	Setpoint_AR3_RTD3_PickupProtecao	AT%MW1756: REAL;
	(*04x14047*)	Setpoint_AR3_RTD4_PickupProtecao	AT%MW1758: REAL;
 	(*04x14049*)	Setpoint_AR4_RTD1_PickupProtecao	AT%MW1760: REAL;
	(*04x14051*)	Setpoint_AR4_RTD2_PickupProtecao	AT%MW1762: REAL;
	(*04x14053*)	Setpoint_AR4_RTD3_PickupProtecao	AT%MW1764: REAL;
	(*04x14055*)	Setpoint_AR4_RTD4_PickupProtecao	AT%MW1766: REAL;
 	(*04x14057*)	Setpoint_AR5_RTD1_PickupProtecao	AT%MW1768: REAL;
	(*04x14059*)	Setpoint_AR5_RTD2_PickupProtecao	AT%MW1770: REAL;
	(*04x14061*)	Setpoint_AR5_RTD3_PickupProtecao	AT%MW1772: REAL;
	(*04x14063*)	Setpoint_AR5_RTD4_PickupProtecao	AT%MW1774: REAL;
 	(*04x14065*)	Setpoint_AR6_RTD1_PickupProtecao	AT%MW1776: REAL;
	(*04x14067*)	Setpoint_AR6_RTD2_PickupProtecao	AT%MW1778: REAL;
	(*04x14069*)	Setpoint_AR6_RTD3_PickupProtecao	AT%MW1780: REAL;
	(*04x14071*)	Setpoint_AR6_RTD4_PickupProtecao	AT%MW1782: REAL;
 	(*04x14073*)	Setpoint_AR7_RTD1_PickupProtecao	AT%MW1784: REAL;
	(*04x14075*)	Setpoint_AR7_RTD2_PickupProtecao	AT%MW1786: REAL;
	(*04x14077*)	Setpoint_AR7_RTD3_PickupProtecao	AT%MW1788: REAL;
	(*04x14079*)	Setpoint_AR7_RTD4_PickupProtecao	AT%MW1790: REAL;
 	(*04x14081*)	Setpoint_AR8_RTD1_PickupProtecao	AT%MW1792: REAL;
	(*04x14083*)	Setpoint_AR8_RTD2_PickupProtecao	AT%MW1794: REAL;
	(*04x14085*)	Setpoint_AR8_RTD3_PickupProtecao	AT%MW1796: REAL;
	(*04x14087*)	Setpoint_AR8_RTD4_PickupProtecao	AT%MW1798: REAL;
       (*04x14089*)	Reserva_14089							AT%MW1800: REAL;
 	(*04x14091*)	Reserva_14091							AT%MW1802: REAL;
       (*04x14093*)	Reserva_14093							AT%MW1804: REAL;
       (*04x14095*)	Reserva_14095							AT%MW1806: REAL;
	(*04x14097*)	Reserva_14097							AT%MW1808: REAL;

        (* --> Tabela de Leituras Retentivas <-- *)
	(*04x14099*)	Horimetro_Mecanico_Total 			AT%MW1810: REAL;
	(*04x14101*)	Horimetro_Mecanico_Atual			AT%MW1812: REAL;
	(*04x14103*)	Horimetro_Mecanico_Ultimo			AT%MW1814: REAL;
	(*04x14105*)	Horimetro_Eletrico_Total				AT%MW1816: REAL;
	(*04x14107*)	Horimetro_Eletrico_Atual				AT%MW1818: REAL;
	(*04x14109*)	Horimetro_Eletrico_Ultimo			AT%MW1820: REAL;
	(*04x14111*)	Horimetro_UHRV_Total				AT%MW1822: REAL;
	(*04x14113*)	Horimetro_UHRV_Atual				AT%MW1824: REAL;
	(*04x14115*)	Horimetro_UHRV_Ultimo				AT%MW1826: REAL;
	(*04x14117*)	Horimetro_UHLM_Total				AT%MW1828: REAL;
	(*04x14119*)	Horimetro_UHLM_Atual				AT%MW1830: REAL;
	(*04x14121*)	Horimetro_UHLM_Ultimo				AT%MW1832: REAL;
'''
horimetro = '''
(*04x13383*)	Gerador_EnergiaFornecidakWh								AT%MW1094: REAL;
(*04x13385*)	Gerador_EnergiaFornecidaMWh								AT%MW1096: REAL;
(*04x13387*)	Gerador_EnergiaFornecidaGWh								AT%MW1098: REAL;
(*04x13389*)	Gerador_EnergiaFornecidakVArh							AT%MW1100: REAL;
(*04x13391*)	Gerador_EnergiaFornecidaMVArh							AT%MW1102: REAL;
(*04x13393*)	Gerador_EnergiaFornecidaGVArh							AT%MW1104: REAL;
(*04x13395*)	Gerador_EnergiaConsumidakWh							AT%MW1106: REAL;
(*04x13397*)	Gerador_EnergiaConsumidaMWh							AT%MW1108: REAL;
(*04x13399*)	Gerador_EnergiaConsumidaGWh							AT%MW1110: REAL;
(*04x13401*)	Gerador_EnergiaConsumidakVArh							AT%MW1112: REAL;
(*04x13403*)	Gerador_EnergiaConsumidaMVArh							AT%MW1114: REAL;
(*04x13405*)	Gerador_EnergiaConsumidaGVArh							AT%MW1116: REAL;
'''

TagsJasp = {
    'comandos': comandos,
    'status': status,
    'leituras': leituras,
    'setpoints': setpoints,
    'horimetro': horimetro
}