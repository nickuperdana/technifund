import pandas as pd
import os
import time

class BrokerFee:
    def __init__(self, buyfee, sellfee):
        self.buy_fee = buyfee
        self.sell_fee = sellfee

class Setting_BrokerFee:
    def __init__(self):
        self.broker_fee = []
    
    def adding_brokerfee(self, bfees, sfees):
        self.bfee_to_add = bfees
        self.sfee_to_add = sfees
        new_entry = BrokerFee(buyfee=self.bfee_to_add, sellfee=self.sfee_to_add)
        self.broker_fee = new_entry
        print(f'"Buy-fee" and "Sell-fee" has been set to {round((self.bfee_to_add)*100, 2)}% and {round((self.sfee_to_add)*100, 2)}%.')
        
    def mod_brokerfee(self):
        input_bfee = self.input_bfee_funct()
        input_sfee = self.input_sfee_funct()
        self.adding_brokerfee(bfees=round(input_bfee/100, 4), sfees=round(input_sfee/100, 4))
        
    def config_bsf(self):
        while True:
            print(f'''Do you want to configure broker's buy and sell-fee percentage?

Description:
- Buy-fee: Cost of share purchase, charged by broker from your buy
  transaction
- Sell-fee: Cost of share selling commission, deducted by broker from
  your sell transaction

If you choose no [N], system by default will set the buy-fee and sell-fee rate at\n{0.15}% and {0.25}% (You can change it later)''')
            set_bsf = str(input("[Y/N]: "))
            if set_bsf.upper() == 'N':
                self.adding_brokerfee(bfees=(0.15 / 100), sfees=(0.25 / 100))
                clear_terminal(0.5)
                break
            elif set_bsf.upper() == 'Y':
                self.mod_brokerfee()
                clear_terminal(0)
                break
            else:
                clear_terminal(0)
                print(f'''{version()}
Welcome to TechniFund (alpha version), your handy investment companion.\n
Before we start, we have to complete prior setup for configuring the\nbroker fee as a fundamental parameter for this program.''')
    
    def menu_one(self):
        bfee = self.broker_fee.buy_fee
        sfee = self.broker_fee.sell_fee
        print(f'''Description:
- Buy-fee: Cost of share purchase, charged from a buy transaction by broker
- Sell-fee: Cost of share selling commission, deducted from a sell
  transaction by broker

> Current buy-fee rate : {bfee} ({round(bfee*100, 2)}%)
> Current sell-fee rate: {sfee} ({round(sfee*100, 2)}%)
''')
        while True:
            user_input = str(input('Press [Y] to continue editing, or any key to cancel: '))
            if user_input.upper() == 'Y':
                self.mod_brokerfee()
                clear_terminal(1)
                break
            else:
                clear_terminal(0)
                break
    
    def input_bfee_funct(self):
        fix = 0
        while True:
            try:
                input_bfee = float(input("Enter value in percentage for buy-fee rate (0.XX): "))
                if input_bfee < 0.01:
                    input_bfee_times_hundred = round(input_bfee * 100, 2)
                    print(f'''
You tried to input {input_bfee}, while asked for 0.xx formatted number.
[1] I understand, keep the buy-fee rate as {input_bfee} percent
[2] My bad, I mean {input_bfee_times_hundred} percent''')
                    option = 0
                    while True:
                        try:
                            select_input = int(input('Select option: '))
                            if select_input == 1:
                                option = 1
                                break
                            elif select_input == 2:
                                option = 2
                                break
                            else:
                                pass
                        except:
                            num_only_please()
                    fix = input_bfee if option == 1 else input_bfee_times_hundred
                else:
                    fix = round(input_bfee, 2)
                return fix
            except:
                num_only_please()
                
    def input_sfee_funct(self):
        fix = 0
        while True:
            try:
                input_sfee = float(input("Enter value in percentage for sell-fee rate (0.XX): "))
                if input_sfee < 0.01:
                    input_sfee_times_hundred = round(input_sfee * 100, 2)
                    print(f'''
You tried to input {input_sfee}, while asked 0.xx formatted number.
[1] I understand, keep the sell-fee rate as {input_sfee} percent
[2] My bad, I mean {input_sfee_times_hundred} percent''')
                    option = 0
                    while True:
                        try:
                            select_input = int(input('Select option: '))
                            if select_input == 1:
                                option = 1
                                break
                            elif select_input == 2:
                                option = 2
                                break
                            else:
                                pass
                        except:
                            num_only_please()
                    fix = input_sfee if option == 1 else input_sfee_times_hundred
                else:
                    fix = round(input_sfee, 2)
                return fix
            except:
                num_only_please()
        
class ProfitCalculator:
    def __init__(self, i_stock, i_qty, i_buy, i_sell, i_gl, i_pgl, i_tbuy, i_bf, i_nbuy, i_tsell, i_sf, i_nsell, i_gol, i_pgol, i_ngol, i_pngol):
        self.stock = i_stock
        self.lot = i_qty
        self.buy_price = i_buy
        self.sell_price = i_sell
        self.price_gain_or_loss = i_gl
        self.perc_price_gain_or_loss = i_pgl
        self.total_buy = i_tbuy
        self.br_buyfee = i_bf
        self.net_buy = i_nbuy
        self.total_sell = i_tsell
        self.br_sellfee = i_sf
        self.net_sell = i_nsell
        self.gain_loss = i_gol
        self.perc_gain_loss = i_pgol
        self.net_gain_loss = i_ngol
        self.perc_net_gain_loss = i_pngol

class Setting_ProfitCalculator:
    def __init__(self):
        self.profit_calculator = []
    
    def calc_profit_calculator(self, stc, qty, buy, sell):
        self.stock_name = stc
        self.lots = qty
        self.buy_prc = buy
        self.sell_prc = sell
        self.price_diff = sell - buy
        self.price_diff_pct = round((self.price_diff) / buy, 4)
        self.tot_buy = qty * 100 * buy
        self.broker_buyfee = self.tot_buy * setting_broker.broker_fee.buy_fee
        self.n_buy = self.tot_buy + self.broker_buyfee
        self.tot_sell = qty * 100 * sell
        self.broker_sellfee = self.tot_sell * setting_broker.broker_fee.sell_fee
        self.n_sell = self.tot_sell - self.broker_sellfee
        self.g_or_l = self.tot_sell - self.tot_buy
        self.perc_g_or_l = round((self.g_or_l)/self.tot_buy, 4)
        self.n_gorl = self.n_sell - self.n_buy
        self.perc_n_gorl = round(self.n_gorl/self.n_buy, 4)
        entry = ProfitCalculator(i_stock=self.stock_name, i_qty=self.lots, i_buy=self.buy_prc, i_sell=self.sell_prc, i_gl=self.price_diff, i_pgl=self.price_diff_pct, i_tbuy=self.tot_buy, i_bf=self.broker_buyfee, i_nbuy=self.n_buy, i_tsell=self.tot_sell, i_sf=self.broker_sellfee, i_nsell=self.n_sell, i_gol=self.g_or_l, i_pgol=self.perc_g_or_l, i_ngol=self.n_gorl, i_pngol=self.perc_n_gorl)
        self.profit_calculator.append(entry)
        
    def calc_input_menu_two(self, stock, qty, bprice, sprice):
        self.calc_profit_calculator(stc=stock, qty=qty, buy=bprice, sell=sprice)
        
        print(f'''Result: 
---
Stock Name: {stock}
Lot(s)    : {qty}
Buy price : {bprice}
Sell price: {sprice}

Price {'loss' if self.profit_calculator[-1].price_gain_or_loss < 0 else 'gain'}: {self.profit_calculator[-1].price_gain_or_loss} ({round(self.profit_calculator[-1].perc_price_gain_or_loss * 100, 2)}%)
Total buy : {self.profit_calculator[-1].total_buy}
Buy-fee   : {self.profit_calculator[-1].br_buyfee} ({round(setting_broker.broker_fee.buy_fee * 100, 2)}%)
Net buy   : {self.profit_calculator[-1].net_buy}
Total sell: {self.profit_calculator[-1].total_sell}
Sell-fee  : {self.profit_calculator[-1].br_sellfee} ({round(setting_broker.broker_fee.sell_fee * 100, 2)}%)
Net sell  : {self.profit_calculator[-1].net_sell}

{'Loss' if self.profit_calculator[-1].gain_loss < 0 else 'Gain'}      : {self.profit_calculator[-1].gain_loss} ({round(self.profit_calculator[-1].perc_gain_loss * 100, 2)}%)
Net {'loss' if self.profit_calculator[-1].net_gain_loss < 0 else 'gain'}  : {round(self.profit_calculator[-1].net_gain_loss, 2)} ({round(self.profit_calculator[-1].perc_net_gain_loss * 100, 2)}%)
''')
    
    def menu_two(self):
        while True:
            print(f'''{version()}
>> [X.2] Profit Calculator:

Description:
Here you can track and estimate your trade outcome based on the\ndetails of stock name, qty (in lots), long/buy price, and short/sell price.\n''')
            u_input_stock = str(input("Enter stock name: "))
            u_input_qty = self.input_qty_func()
            u_input_bprice = self.input_bprice_func()
            u_input_sprice = self.input_sprice_func()
            clear_terminal(0)
            print(f'''{version()}
>> [X.2] Profit Calculator:

Description:
Here you can track and estimate your trade outcome based on the\ndetails of stock name, qty (in lots), long/buy price, and short/sell price.\n''')
            self.calc_input_menu_two(stock=u_input_stock.upper(), qty=u_input_qty, bprice=u_input_bprice, sprice=u_input_sprice)
            user_input = str(input('''---
Press:
[SQ] to save the result and quit calculator,
[S] to save the result and reset calculator,
[Q] to unsave the result and quit calculator,
or other to unsave the result and reset calculator: '''))
            if user_input.upper() == 'SQ':
                clear_terminal(0)
                break
            elif user_input.upper() == 'S':
                clear_terminal(0)
            elif user_input.upper() == 'Q':
                self.profit_calculator.pop()
                clear_terminal(0)
                break
            else:
                self.profit_calculator.pop()
                clear_terminal(0)
                
    def input_qty_func(self):
        while True:
            try:
                u_input_qty = int(input("Enter stock qty (lots): "))
                return u_input_qty
            except:
                num_only_please()
                
    def input_bprice_func(self):
        while True:
            try:
                u_input_bprice = int(input("Enter buy price: "))
                return u_input_bprice
            except:
                num_only_please()
                
    def input_sprice_func(self):
        while True:
            try:
                u_input_sprice = int(input("Enter sell price: "))
                return u_input_sprice
            except:
                num_only_please()
    
class AverageCalculator:
    def __init__(self, i_stock, i_lot, i_price, i_totalbuy, i_netbuy):
        self.acf_stock = i_stock
        self.acf_lot = i_lot
        self.acf_price = i_price
        self.acf_total_buy = i_totalbuy
        self.acf_net_buy = i_netbuy

class Calc_AverageCalculator:
    def __init__(self, i_stock, i_lot, i_totbuy, i_netbuy, i_firstavg, i_finalavg, i_avgsts, i_sprice, i_buyfee, i_totsell, i_netsell, i_sellfee, i_proflos, i_proflosperc, i_netproflos, i_netproflosperc):
        self.cac_stock = i_stock
        self.cac_lot = i_lot
        self.cac_tot_buy = i_totbuy
        self.cac_net_buy = i_netbuy
        self.cac_first_avg = i_firstavg
        self.cac_final_avg = i_finalavg
        self.cac_avgstts = i_avgsts
        self.cac_sprice = i_sprice
        self.cac_buy_fee = i_buyfee
        self.cac_tot_sell = i_totsell
        self.cac_net_sell = i_netsell
        self.cac_sell_fee = i_sellfee
        self.cac_prof_los = i_proflos
        self.cac_prof_los_perc = i_proflosperc
        self.cac_net_prof_los = i_netproflos
        self.cac_net_prof_los_perc = i_netproflosperc

class Setting_AverageCalculator:
    def __init__(self):
        self.average_calculator_frame = []
        self.avg_framer = pd.DataFrame()
        self.avg_calculation = []
        
    def ac_frame_adder(self, stc, qty, prc, tbuy, nbuy):
        self.stock_name = stc
        self.quantity = qty
        self.prices = prc
        self.tot_buy = tbuy
        self.net_buy = nbuy
        entry = AverageCalculator(i_stock=self.stock_name, i_lot=self.quantity, i_price=self.prices, i_totalbuy=self.tot_buy, i_netbuy=self.net_buy)
        self.average_calculator_frame.append(entry)
            
    def prior_menu_three(self):
        to_import = profit_calc.profit_calculator
        list_stock = []
        list_lots = []
        list_price = []
        list_total_buy = []
        list_net_buy = []
        if len(self.average_calculator_frame) == 0 and len(to_import) == 0:
            pass
        elif len(self.average_calculator_frame) == 0 and len(to_import) != 0:
            unique_stock = list(set([to_import[i].stock for i in range(len(to_import))]))
            print(f'''{version()}\n>> [X.3] Averaging Calculator:\n\nWe detected saved entries from menu "Profit Calculator":''')
            for i in range(len(unique_stock)):
                print(f'[{i+1}] {unique_stock[i]}')
            print()
            while True:
                len_notzero_input = input('Choose only one stock name [_] from list above, or [N] to skip import: ')
                try:
                    if int(len_notzero_input) <= len(unique_stock):
                        clear_terminal(0)
                        choice = unique_stock[int(len_notzero_input)-1]
                        print(f'\nImporting {choice} ...')
                        clear_terminal(0)
                        for i in range(len(to_import)):
                            if to_import[i].stock == choice:
                                list_stock.append(to_import[i].stock)
                                list_lots.append(to_import[i].lot)
                                list_price.append(to_import[i].buy_price)
                                list_total_buy.append(to_import[i].total_buy)
                                list_net_buy.append(to_import[i].net_buy)
                            else:
                                pass
                        for i in range(len(list_stock)):
                            self.ac_frame_adder(stc=list_stock[i], qty=list_lots[i], prc=list_price[i], tbuy=list_total_buy[i], nbuy=list_net_buy[i])
                        break
                    else:
                        print('Please input valid option.')
                except:
                    if str(len_notzero_input).upper() == 'N':
                        clear_terminal(0)
                        break
                    else:
                        print('Please input valid option.')
        else:
            pass
        
    def menu_three_framer(self):
        array_obj = self.average_calculator_frame
        if len(array_obj) != 0:
            list_stock = []
            list_lots = []
            list_price = []
            list_total_buy = []
            list_net_buy = []
            for i in range(len(array_obj)):
                list_stock.append(array_obj[i].acf_stock)
                list_lots.append(array_obj[i].acf_lot)
                list_price.append(array_obj[i].acf_price)
                list_total_buy.append(array_obj[i].acf_total_buy)
                list_net_buy.append(array_obj[i].acf_net_buy)
            imp_ac_data = {'Stock':list_stock, 'Lot(s)':list_lots,'Price':list_price,'Total_Buy':list_total_buy,'Net_Buy':list_net_buy}
            table_df = pd.DataFrame(data=imp_ac_data)
            self.avg_framer = table_df
        else:
            pass
    
    def menu_three(self):
        while True:
            print(f'{version()}\n>> [X.3] Averaging Calculator:\n')
            print('Recent import/input:\n')
            frame = self.avg_framer
            array_obj = self.average_calculator_frame
            print("| Stock | Lot(s) | Price | Total_Buy | Net_Buy |\n|            (No recent entries yet)           |\n") if len(array_obj) == 0 else print(frame, '\n')
            print('''---\nMenu:
[A] to input new data/record
[D] to delete any row
[C] to calculate trading average

[Q] to quit''')
            u_input = str(input('Select menu: '))
            if u_input.upper() == 'Q':
                clear_terminal(0)
                break
            elif u_input.upper() == 'A':
                clear_terminal(0)
                self.menu_three_input()
            elif u_input.upper() == 'D':
                clear_terminal(0)
                self.menu_three_delete()
                clear_terminal(0)
            elif u_input.upper() == 'C':
                self.menu_three_calculate_trade()
                clear_terminal(0)
            else:
                clear_terminal(0)
                
    def menu_three_input(self):
        while True:
            print(f'{version()}\n>> [X.3.A] Input new data/record:\n')
            if len(self.average_calculator_frame) == 0:
                u_input_stock = str(input('Enter stock name: ')).upper()
            else:
                u_input_stock = self.average_calculator_frame[-1].acf_stock
                print(f'Enter stock details for {u_input_stock}:\n')
            u_input_qty = self.menu_three_input_qty()
            u_input_price = self.menu_three_input_price()
            stock_tot_buy = u_input_qty * 100 * u_input_price
            stock_net_buy = stock_tot_buy * (1 + setting_broker.broker_fee.buy_fee)
            conf_input = str(input(f'''\n---\nYou have entered this:
Stock Name: {u_input_stock}
Stock qty : {u_input_qty}
Buy Price : {u_input_price}

Press any to proceed input, [R] to cancel and retry input, or [Q] to cancel and quit: '''))
            if conf_input.upper() == 'Q':
                clear_terminal(0)
                break
            elif conf_input.upper() == 'R':
                clear_terminal(0)
            else:
                self.ac_frame_adder(stc=u_input_stock, qty=u_input_qty, prc=u_input_price, tbuy=stock_tot_buy, nbuy=stock_net_buy)
                self.menu_three_framer()
                clear_terminal(0)
                break
        
    def menu_three_input_qty(self):
        while True:
            try:
                u_input_qty = int(input("Enter buy qty (in lots): "))
                return u_input_qty
            except:
                num_only_please()
            
    def menu_three_input_price(self):
        while True:
            try:
                u_input_price = int(input("Enter buying price (per share): "))
                return u_input_price
            except:
                num_only_please()
    
    def menu_three_delete(self):
        while True:
            print(f'{version()}\n>> [X.3.D] Delete any row:\n')
            if len(self.avg_framer) != 0:
                print(f'Recent import/input:\n\n{self.avg_framer}\n')
                u_input_del = input(f'''How to delete row(s):
[a] to delete a single data in index a (e.g. "1"),
[a-b] to delete data in index a to b (e.g. "1-2"),
[a, b, c] to delete data in index a, b, and c, (e.g. "1, 2, 3" or "1,2,3"),

or [Q] to cancel or quit
Delete row: ''')
                try:
                    ui_del_int = int(u_input_del)
                    try:
                        while True:
                            clear_terminal(0)
                            print(f'{version()}\n>> [X.3.D] Delete any row:\n')
                            conf_inddel_inp = input(f'''Warning: You are about to delete this row:
\n{self.avg_framer.loc[[ui_del_int]]}\n
Press [Y] to continue deletion, or [N] to cancel: ''')
                            if str(conf_inddel_inp).upper() == 'N':
                                clear_terminal(0)
                                break
                            elif str(conf_inddel_inp).upper() == 'Y':
                                if len(self.average_calculator_frame) == 1:
                                    average_calc.average_calculator_frame = []
                                    average_calc.avg_framer = pd.DataFrame()
                                    clear_terminal(0)
                                    break
                                else:
                                    self.average_calculator_frame.pop(ui_del_int)
                                    average_calc.prior_menu_three()
                                    average_calc.menu_three_framer()
                                    clear_terminal(0)
                                    break
                            else:
                                pass
                    except:
                        clear_terminal(0)
                        print(f'{version()}\n>> [X.3.D] Delete any row:\n\nPlease input valid index value.\n')
                        clear_terminal(2)
                except:
                    ui_del_str = str(u_input_del)
                    if ui_del_str.upper() == 'Q':
                        clear_terminal(0)
                        break
                    elif "-" in ui_del_str:
                        list_range = [e.strip() for e in ui_del_str.split('-')]
                        try:
                            range_del = list(range(int(list_range[0]), int(list_range[1]) + 1))
                            while len(range_del) != 0:
                                clear_terminal(0)
                                print(f'{version()}\n>> [X.3.D] Delete any row:\n')
                                conf_rangedel_inp = input(f'''Warning: You are about to delete these rows:
\n{self.avg_framer.loc[range_del]}\n
Press [Y] to continue deletion, or [N] to cancel: ''')
                                if str(conf_rangedel_inp).upper() == 'N':
                                    clear_terminal(0)
                                    break
                                elif str(conf_rangedel_inp).upper() == 'Y':
                                    if len(self.average_calculator_frame) == len(range_del):
                                        average_calc.average_calculator_frame = []
                                        average_calc.avg_framer = pd.DataFrame()
                                        clear_terminal(0)
                                        break
                                    else:
                                        for i in range_del:
                                            self.average_calculator_frame.pop(range_del[0])
                                        average_calc.prior_menu_three()
                                        average_calc.menu_three_framer()
                                        clear_terminal(0)
                                        break
                                else:
                                    pass
                            else:
                                clear_terminal(0)
                                print(f'{version()}\n>> [X.3.D] Delete any row:\n\nPlease input valid index range.\n')
                                clear_terminal(2)
                        except:
                            clear_terminal(0)
                            print(f'{version()}\n>> [X.3.D] Delete any row:\n\nPlease input valid index range.\n')
                            clear_terminal(2) 
                    elif "," in ui_del_str:
                        try:
                            list_uniq_select = sorted(list(set([int(e.strip()) for e in ui_del_str.split(',')])))
                            while True:
                                clear_terminal(0)
                                print(f'{version()}\n>> [X.3.D] Delete any row:\n')
                                conf_idselect_inp = input(f'''Warning: You are about to delete these rows:
\n{self.avg_framer.loc[list_uniq_select]}\n{list_uniq_select}
Press [Y] to continue deletion, or [N] to cancel: ''')
                                if str(conf_idselect_inp).upper() == 'N':
                                    clear_terminal(0)
                                    break
                                elif str(conf_idselect_inp).upper() == 'Y':
                                    for i in sorted(list_uniq_select, reverse=True):
                                        self.average_calculator_frame.pop(i)
                                    average_calc.prior_menu_three()
                                    average_calc.menu_three_framer()
                                    clear_terminal(0)
                                    break
                                else:
                                    pass
                        except:
                            clear_terminal(0)
                            print(f'{version()}\n>> [X.3.D] Delete any row:\n\nPlease input valid index value.\n')
                            clear_terminal(2)
                    else:
                        clear_terminal(0)
                        print(f'{version()}\n>> [X.3.D] Delete any row:\n\nPlease input valid option as shown examples.\n')
                        clear_terminal(2)
            else:
                input('No entry/data for deletetion.\n\nPress any to continue: ')
                clear_terminal(0)
                break
    
    def calc_average_calculator(self, stc, lot, tbuy, nbuy, firstavg, fnlavg, avgstts, sprice):
        self.ent_stock = stc
        self.ent_lot = lot
        self.ent_tot_buy = tbuy
        self.ent_net_buy = nbuy
        self.ent_first_avg = firstavg
        self.ent_final_avg = fnlavg
        self.ent_avg_status = avgstts
        self.ent_sprice = sprice
        self.ent_buy_fee = self.ent_net_buy - self.ent_tot_buy
        self.ent_tot_sell = self.ent_lot * 100 * self.ent_sprice
        self.ent_net_sell = self.ent_tot_sell * (1 - setting_broker.broker_fee.buy_fee)
        self.ent_sell_fee = self.ent_tot_sell - self.ent_net_sell
        self.ent_prof_los = self.ent_tot_sell - self.ent_net_buy
        self.ent_prof_los_perc = self.ent_prof_los / self.ent_net_buy
        self.ent_net_prof_los = self.ent_net_sell - self.ent_net_buy
        self.ent_net_prof_los_perc = self.ent_net_prof_los / self.ent_net_buy
        entry = Calc_AverageCalculator(i_stock=self.ent_stock, i_lot=self.ent_lot, i_totbuy=self.ent_tot_buy, i_netbuy=self.ent_net_buy, i_firstavg=self.ent_first_avg, i_finalavg=self.ent_final_avg, i_avgsts=self.ent_avg_status, i_sprice=self.ent_sprice, i_buyfee=self.ent_buy_fee, i_totsell=self.ent_tot_sell, i_netsell=self.ent_net_sell, i_sellfee=self.ent_sell_fee, i_proflos=self.ent_prof_los, i_proflosperc=self.ent_prof_los_perc, i_netproflos=self.ent_net_prof_los, i_netproflosperc=self.ent_net_prof_los_perc)
        self.avg_calculation = entry
    
    def result_ca_calculator(self, i_stc, i_lot, i_tbuy, i_nbuy, i_firstavg, i_fnlavg, i_avgstts, i_sprice):
        self.calc_average_calculator(stc=i_stc, lot=i_lot, tbuy=i_tbuy, nbuy=i_nbuy, firstavg=i_firstavg, fnlavg=i_fnlavg, avgstts=i_avgstts, sprice=i_sprice)
        print(f'''{version()}\n>> [X.3.C] Calculate trading average:\n\nRecent import/input:\n\n{self.avg_framer}\n\n\nResult:
---
Stock name: {self.avg_calculation.cac_stock}
Total lots: {self.avg_calculation.cac_lot}
Entry avg : {self.avg_calculation.cac_first_avg}
Final avg : {self.avg_calculation.cac_final_avg} ({self.avg_calculation.cac_avgstts})
Sell at   : {self.avg_calculation.cac_sprice}

Total buy : {self.avg_calculation.cac_tot_buy}
Buy-fee   : {round(self.avg_calculation.cac_buy_fee, 2)}
Net buy   : {self.avg_calculation.cac_net_buy}
Total sell: {self.avg_calculation.cac_tot_sell}
Sell-fee  : {round(self.avg_calculation.cac_sell_fee, 2)}
Net sell  : {round(self.avg_calculation.cac_net_sell, 2)}

{'Loss  ' if self.avg_calculation.cac_prof_los < 0 else 'Profit'}    : {round(self.avg_calculation.cac_prof_los, 2)} ({round(self.avg_calculation.cac_prof_los_perc * 100, 2)}%)
{'Net loss  ' if 0 < 0 else 'Net profit'}: {round(self.avg_calculation.cac_net_prof_los, 2)} ({round(self.avg_calculation.cac_net_prof_los_perc * 100, 2)}%)\n\n''')
                                    
    def menu_three_calculate_trade(self):
        while True:
            clear_terminal(0)
            print(f'{version()}\n>> [X.3.C] Calculate trading average:\n')
            first_avg_stts = 'Unchanged'
            if len(self.average_calculator_frame) == 0:
                input('No entry/data for average calculation.\n\nPress any to continue: ')
                clear_terminal(0)
                break
            else: 
                print(f'Recent import/input:\n\n{self.avg_framer}\n\n')
                try:
                    sell_price = int(input('Enter target sell price: '))
                    
                    if len(self.average_calculator_frame) == 1:
                        clear_terminal(0)
                        first_avg = round(self.average_calculator_frame[0].acf_net_buy / (self.average_calculator_frame[0].acf_lot * 100), 2)
                        self.result_ca_calculator(i_stc=self.average_calculator_frame[0].acf_stock, i_lot=self.average_calculator_frame[0].acf_lot, i_tbuy=self.average_calculator_frame[0].acf_total_buy, i_nbuy=self.average_calculator_frame[0].acf_net_buy, i_firstavg=first_avg, i_fnlavg=first_avg, i_avgstts=first_avg_stts, i_sprice=sell_price)
                    else:
                        clear_terminal(0)
                        sum_lot = sum([self.average_calculator_frame[i].acf_lot for i in range(len(self.average_calculator_frame))])
                        first_avg = round(self.average_calculator_frame[0].acf_net_buy / (self.average_calculator_frame[0].acf_lot * 100), 2)
                        final_avg = round(sum([self.average_calculator_frame[i].acf_net_buy for i in range(len(self.average_calculator_frame))]) / (sum_lot * 100), 2)
                        if first_avg == final_avg:
                            pass
                        elif first_avg < final_avg:
                            first_avg_stts = 'Average UP'
                        else:
                            first_avg_stts = 'Average DOWN'
                        ttl_buy = sum([self.average_calculator_frame[i].acf_total_buy for i in range(len(self.average_calculator_frame))])
                        nt_buy = sum([self.average_calculator_frame[i].acf_net_buy for i in range(len(self.average_calculator_frame))])
                        self.result_ca_calculator(i_stc=self.average_calculator_frame[0].acf_stock, i_lot=sum_lot, i_tbuy=ttl_buy, i_nbuy=nt_buy, i_firstavg=first_avg, i_fnlavg=final_avg, i_avgstts=first_avg_stts, i_sprice=sell_price)
                    save_input = str(input('Options:\n[SQ] to save and quit,\n[S] to save and reset,\n[Q] to unsave and quit,\nor other to unsave and reset\n\nSelect option: '))
                    if save_input.upper() == 'SQ':
                        clear_terminal(0)
                        break
                    elif save_input.upper() == 'S':
                        self.avg_calculation = []
                        clear_terminal(0)
                        pass
                    elif save_input.upper() == 'Q':
                        self.avg_calculation = []
                        clear_terminal(0)
                        break
                    else:
                        clear_terminal(0)
                        pass
                except:
                    clear_terminal(0)
                    print()
                    num_only_please()        
            
# border between classes and functions

def clear_terminal(sec):
    time.sleep(sec)
    os.system('cls' if os.name == 'nt' else 'clear')

def version():
    return '<> TechniFund v0.1.1-alpha'

def num_only_please():
    print('Please input numbers only.')

def coming_soon_opt(menu):
    clear_terminal(0)
    print(f"Can't wait to use menu number {menu}, eh? Relax, it will coming soon!\n\nGetting you back to the main menu ...")
    clear_terminal(4)

def su_mem():
    while True:
        clear_terminal(0)
        print(f'''{version()}\n>> [X.SU] Objects saved in memory:\n---\n\n''')
        print('>> [X.1] obj_broker_fee: ')
        print(setting_broker.broker_fee, '\n')
        print('>> [X.2] obj_profit_calculator: ')
        print(profit_calc.profit_calculator, '\n')
        print('>> [X.3] obj_average_calculator_frame: ')
        print(average_calc.average_calculator_frame, '\n')
        print('>> [X.3] obj_average_calculation: ')
        print(average_calc.avg_calculation, '\n')
        print('>> [X.3] obj_avg_framer: ')
        print(average_calc.avg_framer, '\n\n\n---')
        su_mem_input = input('Press any key to exit: ')
        if su_mem_input:
            clear_terminal(0)
            break
        else:
            clear_terminal(0)
            break

def main_menu():
    while True:
        print(f'''{version()}
>> [X] Menu:\n
[1] Edit broker fee setting
[2] Profit Calculator
[3] Averaging Calculator
[4] Scalping/Trading Planner (Coming Soon!)
[5] Dividend Yield Estimator (Coming Soon!)
[6] Money Management (Coming Soon!)\n
[77] Load previous session (Coming soon!)
[88] Save this session (Coming soon!)
[99] About TechniFund
[00] Exit program
''')
        smenu_input = input('Select menu: ')
        try:
            u_input = int(smenu_input)
            if u_input == 1:
                clear_terminal(0)
                print(f'{version()}\n>> [X.1] Edit broker fee setting:\n')
                setting_broker.menu_one()
            elif u_input == 2:
                clear_terminal(0)
                profit_calc.menu_two()
            elif u_input == 3:
                clear_terminal(0)
                average_calc.prior_menu_three()
                average_calc.menu_three_framer()
                average_calc.menu_three()
            elif u_input == 4:
                coming_soon_opt(u_input)
            elif u_input == 5:
                coming_soon_opt(u_input)
            elif u_input == 6:
                coming_soon_opt(u_input)
            elif u_input == 77:
                coming_soon_opt(u_input)
            elif u_input == 88:
                coming_soon_opt(u_input)
            elif u_input == 99:
                coming_soon_opt(u_input)
            elif u_input == 0:
                clear_terminal(0)
                print(f'{version()}\n>> [X.0] Exit program:\n')
                conf_input = input('>> Are you sure want to exit program?\nPress [Y] to exit, or other to cancel: ')
                if conf_input.upper() == 'Y':
                    print('\nExiting program... See you later ...\n')
                    clear_terminal(1)
                    break
                else:
                    clear_terminal(0)
            else:
                clear_terminal(0)
                pass
        except:
            u_input_str = str(smenu_input)
            if u_input_str.upper() == 'SU MEM':
                su_mem()
            else:
                clear_terminal(0)
                print()
                num_only_please()
                print()
                clear_terminal(2)

# border between classes, functions, and main

if __name__ == '__main__':
    os.system("title TechniFund v0.1.1-alpha")
    clear_terminal(0)
    setting_broker = Setting_BrokerFee()
    profit_calc = Setting_ProfitCalculator()
    average_calc = Setting_AverageCalculator()
    print(f'''{version()}
Welcome to TechniFund (alpha version), your handy investment companion.\n
Before we start, we have to complete prior setup for configuring the broker
fee as a fundamental parameter for this program.''')
    setting_broker.config_bsf()
    print('\nApplication starting ...\n')
    clear_terminal(1)
    main_menu()