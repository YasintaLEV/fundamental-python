"""
Tipe data dictionary sekedar menghubungkan antara KEY dan VALUE
KVP = Key Value Pair
Dictionary = Kamus
"""

kamus_ind_eng = {}
kamus_ind_eng ['anak'] = 'son'
kamus_ind_eng ['istri'] = 'wife'
kamus_ind_eng ['ayah'] = 'father'
kamus_ind_eng ['ibu'] = 'mother'

print(kamus_ind_eng)
print(kamus_ind_eng ['ayah'])
print(kamus_ind_eng ['ibu'])
print(kamus_ind_eng ['istri'])
print(kamus_ind_eng ['anak'])

kamus_eng_ind = {'son': ' anak', 'wife': 'istri', 'father': 'ayah', 'mother': ' ibu '}

print(kamus_eng_ind)
print(kamus_eng_ind ['son'])
print(kamus_eng_ind ['wife'])
print(kamus_eng_ind ['father'])
print(kamus_eng_ind ['mother'])

print('\nData ini dikirimkan oleh server Gojek, untuk memberikan info driver di sekitar pemakai aplikasi')
data_dari_server_gojek = {
    'tanggal': '2021-02-27',
    'driver_list': [{'nama' : 'Eko' ,'jarak':10} ,
                    {'nama' :'Dwi' ,'jarak':20} ,
                    {'nama' :'Tri' ,'jarak':500} ,
                    {'nama' :'Catur' ,'jarak': 1000}
                    ]
    }
print(data_dari_server_gojek)
print(f"\nDriver disekitar sini{data_dari_server_gojek['driver_list']}")
print(f"Driver #1 {data_dari_server_gojek['driver_list'][0]}")
print(f"Driver #1 {data_dari_server_gojek['driver_list'][3]}")
print(f'Driver terdekat berjarak {data_dari_server_gojek["driver_list"][0]["jarak"]}  meter')
