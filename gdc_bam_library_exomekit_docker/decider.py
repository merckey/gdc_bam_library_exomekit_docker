import sys

def get_capture_kit(catalog_number, capture_kit):
    cached_target_file_url = capture_kit.get('cached_target_file_url', None)
    catalog_number = capture_kit.get('catalog_number')
    is_custom = capture_kit.get('is_custom', None)
    probe_file_url = capture_kit.get('probe_file_url', None)
    reagent_name = capture_kit.get('reagent_name', None)
    reagent_vendor = capture_kit.get('reagent_vendor', None)
    target_file_url = capture_kit.get('target_file_url', None)

    kit_name = None
    if catalog_number == '05860504001':
        if (cached_target_file_url == 'https://bitbucket.org/cghub/cghub-capture-kit-info/raw/d8b126dd4f33eb7164535e00f0ec9a5985056f34/cache/a6408d236823a1abb63adb8c38caf37442e20109#Design_Annotation_files/Target_Regions/SeqCap_EZ_Exome_v2.bed'):
            if (is_custom == ''):
                if (probe_file_url is None):
                    if (reagent_name == 'Nimblegen SeqCap EZ Human Exome Library v2.0'):
                        if (reagent_vendor == 'Nimblegen'):
                            if (target_file_url == 'http://www.nimblegen.com/downloads/annotation/ez_exome_v2/SeqCapEZ_Exome_v2.0_Design_Annotation_files.zip#Design_Annotation_files/Target_Regions/SeqCap_EZ_Exome_v2.bed'):
                                kit_name = 'SeqCap_EZ_Exome_v2'

    if catalog_number == '06 465 668 001':
        if (cached_target_file_url == 'https://bitbucket.org/cghub/cghub-capture-kit-info/raw/9129b8e749210d4b74a428448e01a6217f94e0ee/cache/d9d1988de1e3131c585cc963a433844953fae95c#VCRome_2_1_hg19_primary_targets.bed' or
            cached_target_file_url == 'https://bitbucket.org/cghub/cghub-capture-kit-info/raw/d8b126dd4f33eb7164535e00f0ec9a5985056f34/cache/d9d1988de1e3131c585cc963a433844953fae95c#VCRome_2_1_hg19_primary_targets.bed' or
            cached_target_file_url == 'https://bitbucket.org/cghub/cghub-capture-kit-info/raw/d993d72ee92cd14de3c4a6da435f4a29e932a9db/cache/d9d1988de1e3131c585cc963a433844953fae95c#VCRome_2_1_hg19_primary_targets.bed'):
            if (is_custom == '' or
                is_custom == 'No'):
                if probe_file_url is None:
                    if (reagent_name == 'VCRome V2.1' or
                        reagent_name == 'SeqCap EZ HGSC VCRome'):
                        if (reagent_vendor == 'Nimblegen' or
                            reagent_vendor == 'NimbleGen'):
                            if target_file_url == 'http://www.nimblegen.com/downloads/annotation/ez_vcrome_nov2014/VCRome_2.1_design_files.zip#VCRome_2_1_hg19_primary_targets.bed':
                                kit_name = 'VCRome_V2.1'

    if catalog_number == '06465692001':
        if (cached_target_file_url == 'https://bitbucket.org/cghub/cghub-capture-kit-info/raw/d8b126dd4f33eb7164535e00f0ec9a5985056f34/cache/9e3d281bb849a36c6134be0e348a027ba81123b4#SeqCap_EZ_Exome_v3_capture.bed'
            or cached_target_file_url is None):
            if (is_custom == '' or
                is_custom is None):
                if probe_file_url is None:
                    if (reagent_name == 'Nimblegen SeqCap EZ Human Exome Library v3.0' or
                        reagent_name == 'Nimblegen EZ Exome v3.0'):
                        if (reagent_vendor == 'Nimblegen'):
                            if target_file_url == 'http://www.nimblegen.com/downloads/annotation/ez_exome_v3/SeqCapEZ_Exome_v3.0_Design_Annotation_files.zip#SeqCap_EZ_Exome_v3_capture.bed':
                                kit_name = 'SeqCap_EZ_Exome_v3'

    if catalog_number == '5860504001':
        if (cached_target_file_url == 'https://bitbucket.org/cghub/cghub-capture-kit-info/raw/d8b126dd4f33eb7164535e00f0ec9a5985056f34/cache/a6408d236823a1abb63adb8c38caf37442e20109#Target_Regions/SeqCap_EZ_Exome_v2.bed' or
            cached_target_file_url == 'https://bitbucket.org/cghub/cghub-capture-kit-info/raw/d993d72ee92cd14de3c4a6da435f4a29e932a9db/cache/a6408d236823a1abb63adb8c38caf37442e20109#Target_Regions/SeqCap_EZ_Exome_v2.bed' or
            cached_target_file_url == 'https://bitbucket.org/cghub/cghub-capture-kit-info/raw/d8b126dd4f33eb7164535e00f0ec9a5985056f34/cache/a6408d236823a1abb63adb8c38caf37442e20109#SeqCap_EZ_Exome_v2.bed' or
            cached_target_file_url == 'https://bitbucket.org/cghub/cghub-capture-kit-info/raw/9129b8e749210d4b74a428448e01a6217f94e0ee/cache/a6408d236823a1abb63adb8c38caf37442e20109#Target_Regions/SeqCap_EZ_Exome_v2.bed'):
            if (is_custom == '' or
                is_custom == 'No'):
                if probe_file_url is None:
                    if (reagent_name == 'SeqCap EZ Human Exome Library v2.0' or
                        reagent_name == 'SeqCap EZ Exome V2.0'):
                        if (reagent_vendor == 'NimbleGen' or
                            reagent_vendor == 'Nimblegen'):
                            if (target_file_url == 'http://www.nimblegen.com/downloads/annotation/ez_exome_v2/SeqCapEZ_Exome_v2.0_Design_Annotation_files.zip#Target_Regions/SeqCap_EZ_Exome_v2.bed' or
                                target_file_url == 'http://www.nimblegen.com/downloads/annotation/ez_exome_v2/SeqCapEZ_Exome_v2.0_Design_Annotation_files.zip#SeqCap_EZ_Exome_v2.bed'):
                                kit_name = 'SeqCap_EZ_Exome_v2'

    if catalog_number == '931070':
        if cached_target_file_url is None:
            if is_custom == '':
                if probe_file_url == 'https://bitbucket.org/cghub/cghub-capture-kit-info/raw/d8b126dd4f33eb7164535e00f0ec9a5985056f34/BI/vendor/Agilent/whole_exome_agilent_1.1_refseq_plus_3_boosters.baitIntervals.bed':
                    if reagent_name == 'Custom V2 Exome Bait, 48 RXN X 16 tubes':
                        if (reagent_vendor == 'Agilent'):
                            if target_file_url == 'https://bitbucket.org/cghub/cghub-capture-kit-info/raw/d8b126dd4f33eb7164535e00f0ec9a5985056f34/BI/vendor/Agilent/whole_exome_agilent_1.1_refseq_plus_3_boosters.targetIntervals.bed':
                                kit_name = 'whole_exome_agilent_1.1_refseq_plus_3_boosters'

    if catalog_number == 'Obsolete':
        if cached_target_file_url == 'https://bitbucket.org/cghub/cghub-capture-kit-info/raw/d8b126dd4f33eb7164535e00f0ec9a5985056f34/cache/6e06f65d203c49a50849780f58a53266d2e30f94#2.1M_Human_Exome.bed':
            if is_custom == '':
                if probe_file_url is None:
                    if reagent_name == 'NimbleGen Sequence Capture 2.1M Human Exome Array':
                        if reagent_vendor == 'Nimblegen':
                            if target_file_url == 'http://www.nimblegen.com/downloads/annotation/seqcap_exome/2.1M_Human_Exome_Annotation.zip#2.1M_Human_Exome.bed':
                                kit_name = '2.1M_Human_Exome'

    if catalog_number == 'S0293689':
        if (cached_target_file_url is None or
            cached_target_file_url == 'https://bitbucket.org/cghub/cghub-capture-kit-info/raw/d8b126dd4f33eb7164535e00f0ec9a5985056f34/cache/8aa7f3bc5043420868dd7d43e925e7e739d9af76'):
            if (is_custom == '' or
                is_custom is None):
                if probe_file_url is None:
                    if reagent_name == 'SureSelect Human All Exon 38 Mb v2':
                        if reagent_vendor == 'Agilent':
                            if target_file_url == 'https://earray.chem.agilent.com/earray/':
                                 kit_name = 'SureSelect_Human_All_Exon_38_Mb_v2'

    if catalog_number == 'S02972011':
        if cached_target_file_url == 'https://bitbucket.org/cghub/cghub-capture-kit-info/raw/d8b126dd4f33eb7164535e00f0ec9a5985056f34/cache/8aa7f3bc5043420868dd7d43e925e7e739d9af76':
            if is_custom == '':
                if probe_file_url is None:
                    if reagent_name == 'SureSelect Human All Exon 50Mb Kit':
                        if reagent_vendor == 'Agilent':
                            if target_file_url == 'https://earray.chem.agilent.com/earray/':
                                kit_name = 'SureSelect_Human_All_Exon_50Mb_Kit'

    if catalog_number == 'S04380110':
        if cached_target_file_url is None:
            if is_custom == '':
                if probe_file_url == 'https://earray.chem.agilent.com/suredesign/':
                    if reagent_name == 'SureSelectXT Human All Exon V5, 16':
                        if reagent_vendor == 'Agilent':
                            if target_file_url == 'https://earray.chem.agilent.com/suredesign/':
                                kit_name = 'SureSelectXT_Human_All_Exon_V5_16'

    if catalog_number == 'NA':
        if (cached_target_file_url == 'https://bitbucket.org/cghub/cghub-capture-kit-info/raw/9129b8e749210d4b74a428448e01a6217f94e0ee/cache/bc1f300fe8bb51f8b0e4df318392d84b691d9d73' or
            cached_target_file_url == 'https://bitbucket.org/cghub/cghub-capture-kit-info/raw/d993d72ee92cd14de3c4a6da435f4a29e932a9db/cache/bc1f300fe8bb51f8b0e4df318392d84b691d9d73' or
            cached_target_file_url == 'https://bitbucket.org/cghub/cghub-capture-kit-info/raw/d8b126dd4f33eb7164535e00f0ec9a5985056f34/cache/bc1f300fe8bb51f8b0e4df318392d84b691d9d73'):
            if (is_custom == 'yes'):
                if (probe_file_url is None):
                    if (reagent_name == 'VCRomeV2.1-PKv1' or
                        reagent_name == 'VCRome V2.1-PKv1' or
                        reagent_name == 'Gapfiller_7m'):
                        if (reagent_vendor == 'Nimblegen'):
                            if (target_file_url == 'http://www.nimblegen.com/index.html'):
                                kit_name = 'VCRomeV2.1-PKv1'

        if (cached_target_file_url == 'https://bitbucket.org/cghub/cghub-capture-kit-info/raw/d8b126dd4f33eb7164535e00f0ec9a5985056f34/cache/11f8abd6c1d46c06664588b4ca6945715a324139'):
            if (is_custom == ''):
                if (probe_file_url is None):
                    if (reagent_name == '120613_HG19_EC_HPV_39235 capture oligo tube'):
                        if (reagent_vendor == 'IDT'):
                            if (target_file_url == 'ftp://genome.wustl.edu/pub/custom_capture/120613_HG19_EC_HPV_39235_capture_oligo_tube/6D44F569CD1711E1AFBE5C7646F0A7A3.bed'):
                                kit_name = '120613_HG19_EC_HPV_39235_capture_oligo_tube'

        if (cached_target_file_url == 'https://bitbucket.org/cghub/cghub-capture-kit-info/raw/d8b126dd4f33eb7164535e00f0ec9a5985056f34/cache/4a4c74119a93ac880db4f48ed5ef0b2c72abac4f'):
            if (is_custom == ''):
                if (probe_file_url is None):
                    if (reagent_name == 'WO2790654 pooled probes'):
                        if (reagent_vendor == 'IDT'):
                            if (target_file_url == 'ftp://genome.wustl.edu/pub/custom_capture/WO2790654_pooled_probes/1d60152280514553b6a01cd20d2b12e8.bed'):
                                kit_name = 'WO2790654_pooled_probes'

        if (cached_target_file_url == 'https://bitbucket.org/cghub/cghub-capture-kit-info/raw/d8b126dd4f33eb7164535e00f0ec9a5985056f34/cache/bb414b0a19ecf13ff83a1513a3fe1966e45b12d1'):
            if (is_custom == ''):
                if (probe_file_url is None):
                    if (reagent_name == 'RT42434_pool_3'):
                        if (reagent_vendor == 'Agilent'):
                            if (target_file_url == 'ftp://genome.wustl.edu/pub/custom_capture/RT42434_pool_3/RT42434_pool_3.bed'):
                                kit_name = 'RT42434_pool_3'

        if (cached_target_file_url == 'https://bitbucket.org/cghub/cghub-capture-kit-info/raw/d8b126dd4f33eb7164535e00f0ec9a5985056f34/cache/ce6ca462d83586653ba0c93826b957a4ed20f657'):
            if (is_custom == ''):
                if (probe_file_url is None):
                    if (reagent_name == 'RT42434_pool_2'):
                        if (reagent_vendor == 'Agilent'):
                            if (target_file_url == 'ftp://genome.wustl.edu/pub/custom_capture/RT42434_pool_2/RT42434_pool_2.bed'):
                                kit_name = 'RT42434_pool_2'

        if (cached_target_file_url == 'https://bitbucket.org/cghub/cghub-capture-kit-info/raw/d8b126dd4f33eb7164535e00f0ec9a5985056f34/cache/7907a67ea1ea4c0597b798fe76e0784fdfc5a775'):
            if (is_custom == ''):
                if (probe_file_url is None):
                    if (reagent_name == 'WO2736953 pooled probes'):
                        if (reagent_vendor == 'IDT'):
                            if (target_file_url == 'ftp://genome.wustl.edu/pub/custom_capture/WO2736953_pooled_probes/784c240d7e6942afb8514ebdb6a950d9.bed'):
                                kit_name = 'WO2736953_pooled_probes'

        if (cached_target_file_url == 'https://bitbucket.org/cghub/cghub-capture-kit-info/raw/d8b126dd4f33eb7164535e00f0ec9a5985056f34/cache/e85c146001353997a2456d7304d9a25bcb43be8a'):
            if (is_custom == ''):
                if (probe_file_url is None):
                    if (reagent_name == 'HPV_IDT_probes capture chip set'):
                        if (reagent_vendor == 'IDT'):
                            if (target_file_url == 'ftp://genome.wustl.edu/pub/custom_capture/HPV_IDT_probes_capture_chip_set/AC6217418DAB11E1BD99FC55D6BB89D5.bed'):
                                kit_name = 'HPV_IDT_probes_capture_chip_set'

        if (cached_target_file_url == 'https://bitbucket.org/cghub/cghub-capture-kit-info/raw/d8b126dd4f33eb7164535e00f0ec9a5985056f34/cache/50c5194ab0ea02c9df3b2f9f3b43134eb2883a0f'):
            if (is_custom == ''):
                if (probe_file_url is None):
                    if (reagent_name == 'hg18 nimblegen exome version 2'):
                        if (reagent_vendor == 'Nimblegen'):
                            if (target_file_url == 'ftp://genome.wustl.edu/pub/custom_capture/hg18_nimblegen_exome_version_2/hg18_nimblegen_exome_version_2.bed'):
                                kit_name = 'hg18_nimblegen_exome_version_2'

        if (cached_target_file_url == 'https://bitbucket.org/cghub/cghub-capture-kit-info/raw/d8b126dd4f33eb7164535e00f0ec9a5985056f34/cache/b1888969f61a2f718e9d6d05879c5ea8f8e436f4'):
            if (is_custom == ''):
                if (probe_file_url is None):
                    if (reagent_name == 'TCGA OV Reorder high'):
                        if (reagent_vendor == 'Agilent'):
                            if (target_file_url == 'ftp://genome.wustl.edu/pub/custom_capture/TCGA_OV_Reorder_high/TCGA_OV_Reorder_high.bed'):
                                kit_name = 'TCGA_OV_Reorder_high'

        if (cached_target_file_url == 'https://bitbucket.org/cghub/cghub-capture-kit-info/raw/d8b126dd4f33eb7164535e00f0ec9a5985056f34/cache/8a3fcc6223463ce7b5de285792d435aa620001a5'):
            if (is_custom == ''):
                if (probe_file_url is None):
                    if (reagent_name == 'WO2791991 pooled probes'):
                        if (reagent_vendor == 'IDT'):
                            if (target_file_url == 'ftp://genome.wustl.edu/pub/custom_capture/WO2791991_pooled_probes/ce2c7958845b4895b878a6eda8a9c521.bed'):
                                kit_name = 'WO2791991_pooled_probes'

        if (cached_target_file_url == 'https://bitbucket.org/cghub/cghub-capture-kit-info/raw/d8b126dd4f33eb7164535e00f0ec9a5985056f34/cache/2d8b911f7c67e07ea4bf120a7ed3c8dd8b9d206a'):
            if (is_custom == ''):
                if (probe_file_url is None):
                    if (reagent_name == 'WO2830729 pooled probes'):
                        if (reagent_vendor == 'IDT'):
                            if (target_file_url == 'ftp://genome.wustl.edu/pub/custom_capture/WO2830729_pooled_probes/fe74a5ca10fc4f378a733cdfd308b130.bed'):
                                kit_name = 'WO2830729_pooled_probes'

        if (cached_target_file_url == 'https://bitbucket.org/cghub/cghub-capture-kit-info/raw/d8b126dd4f33eb7164535e00f0ec9a5985056f34/cache/2068a546e396d1500f5fd835857c6e933a1d84b5'):
            if (is_custom == ''):
                if (probe_file_url is None):
                    if (reagent_name == 'HBV_IDT_probes pooled probes'):
                        if (reagent_vendor == 'IDT'):
                            if (target_file_url == 'ftp://genome.wustl.edu/pub/custom_capture/HBV_IDT_probes_pooled_probes/40774c8461274a81b4d223161dc84936.bed'):
                                kit_name = 'HBV_IDT_probes_pooled_probes'

        if (cached_target_file_url == 'https://bitbucket.org/cghub/cghub-capture-kit-info/raw/d8b126dd4f33eb7164535e00f0ec9a5985056f34/cache/f5394a4f818ecc116206d687fcfa0dbc5f912e3d'):
            if (is_custom == ''):
                if (probe_file_url is None):
                    if (reagent_name == 'RT42434_pool_1'):
                        if (reagent_vendor == 'Agilent'):
                            if (target_file_url == 'ftp://genome.wustl.edu/pub/custom_capture/RT42434_pool_1/RT42434_pool_1.bed'):
                                kit_name = 'RT42434_pool_1'

        if (cached_target_file_url == 'https://bitbucket.org/cghub/cghub-capture-kit-info/raw/d8b126dd4f33eb7164535e00f0ec9a5985056f34/cache/ede88294372ca987eaff42020cebc6eb5bf11189'):
            if (is_custom == ''):
                if (probe_file_url is None):
                    if (reagent_name == 'HPV IDT all pooled probes'):
                        if (reagent_vendor == 'IDT'):
                            if (target_file_url == 'ftp://genome.wustl.edu/pub/custom_capture/HPV_IDT_all_pooled_probes/37b1fc41fd114b64b94336ff9b4d97ae.bed'):
                                kit_name = 'HPV_IDT_all_pooled_probes'

        if (cached_target_file_url == 'https://bitbucket.org/cghub/cghub-capture-kit-info/raw/d8b126dd4f33eb7164535e00f0ec9a5985056f34/cache/7e68eadf54d9af4250680f54be920480c1fbe5d1'):
            if (is_custom == ''):
                if (probe_file_url is None):
                    if (reagent_name == 'TCGA OV Reorder lowest'):
                        if (reagent_vendor == 'Agilent'):
                            if (target_file_url == 'ftp://genome.wustl.edu/pub/custom_capture/TCGA_OV_Reorder_lowest/TCGA_OV_Reorder_lowest.bed'):
                                kit_name = 'TCGA_OV_Reorder_lowest'

        if (cached_target_file_url == 'https://bitbucket.org/cghub/cghub-capture-kit-info/raw/d8b126dd4f33eb7164535e00f0ec9a5985056f34/cache/4f7568b17b7e9d6b4f24025fdbb30c7d7cd8b56a'):
            if (is_custom == ''):
                if (probe_file_url is None):
                    if (reagent_name == 'RT42434_pool_1b'):
                        if (reagent_vendor == 'Agilent'):
                            if (target_file_url == 'ftp://genome.wustl.edu/pub/custom_capture/RT42434_pool_1b/RT42434_pool_1b.bed'):
                                kit_name = 'RT42434_pool_1b'

        if (cached_target_file_url == 'https://bitbucket.org/cghub/cghub-capture-kit-info/raw/d8b126dd4f33eb7164535e00f0ec9a5985056f34/cache/33f1f212a9bcdb0b637ef916074b0b2644bb7515'):
            if (is_custom == ''):
                if (probe_file_url is None):
                    if (reagent_name == 'TCGA OV Reorder highest'):
                        if (reagent_vendor == 'Agilent'):
                            if (target_file_url == 'ftp://genome.wustl.edu/pub/custom_capture/TCGA_OV_Reorder_highest/TCGA_OV_Reorder_highest.bed'):
                                kit_name = 'TCGA_OV_Reorder_highest'

        if (cached_target_file_url == 'https://bitbucket.org/cghub/cghub-capture-kit-info/raw/d8b126dd4f33eb7164535e00f0ec9a5985056f34/cache/7d96bdcacb3cc36260542e5b33c39e21c5b6f676'):
            if (is_custom == ''):
                if (probe_file_url is None):
                    if (reagent_name == 'WO2768646 pooled probes'):
                        if (reagent_vendor == 'IDT'):
                            if (target_file_url == 'ftp://genome.wustl.edu/pub/custom_capture/WO2768646_pooled_probes/562e962c09834121a17bf931182c90e7.bed'):
                                kit_name = 'WO2768646_pooled_probes'

        if (cached_target_file_url == 'https://bitbucket.org/cghub/cghub-capture-kit-info/raw/d8b126dd4f33eb7164535e00f0ec9a5985056f34/cache/00b29faf640c3cbd53672784fda3ea7c1faea3c6'):
            if (is_custom == ''):
                if (probe_file_url is None):
                    if (reagent_name == 'TCGA OV Reorder low'):
                        if (reagent_vendor == 'Agilent'):
                            if (target_file_url == 'ftp://genome.wustl.edu/pub/custom_capture/TCGA_OV_Reorder_low/TCGA_OV_Reorder_low.bed'):
                                kit_name = 'TCGA_OV_Reorder_low'

        if (cached_target_file_url == 'https://bitbucket.org/cghub/cghub-capture-kit-info/raw/d8b126dd4f33eb7164535e00f0ec9a5985056f34/cache/32582a06e016cb9258ca53b12b9321d1b70a9409'):
            if (is_custom == ''):
                if (probe_file_url is None):
                    if (reagent_name == 'WO2831284 pooled probes'):
                        if (reagent_vendor == 'IDT'):
                            if (target_file_url == 'ftp://genome.wustl.edu/pub/custom_capture/WO2831284_pooled_probes/b431049e36034157903ae2c75302af2d.bed'):
                                kit_name = 'WO2831284_pooled_probes'

        if (cached_target_file_url == 'https://bitbucket.org/cghub/cghub-capture-kit-info/raw/d8b126dd4f33eb7164535e00f0ec9a5985056f34/cache/f07a90dc0413716e5cebcfe30834f0ac3e0779ec'):
            if (is_custom == ''):
                if (probe_file_url is None):
                    if (reagent_name == 'WO2793950 pooled probes'):
                        if (reagent_vendor == 'IDT'):
                            if (target_file_url == 'ftp://genome.wustl.edu/pub/custom_capture/WO2793950_pooled_probes/0383d24d42694f7a98b17df4f5104b4d.bed'):
                                kit_name = 'WO2793950_pooled_probes'

        if (cached_target_file_url is None):
            if (is_custom == ''):
                if (probe_file_url == 'https://bitbucket.org/cghub/cghub-capture-kit-info/raw/d8b126dd4f33eb7164535e00f0ec9a5985056f34/BI/vendor/Agilent/gabriel_tcga_ovarian_validation_july2010.baitIntervals.bed'):
                    if (reagent_name == 'Custom V2 Exome Bait, 48 RXN X 16 tubes'):
                        if (reagent_vendor == 'Agilent'):
                            if (target_file_url == 'https://bitbucket.org/cghub/cghub-capture-kit-info/raw/d8b126dd4f33eb7164535e00f0ec9a5985056f34/BI/vendor/Agilent/gabriel_tcga_ovarian_validation_july2010.targetIntervals.bed'):
                                kit_name = 'gabriel_tcga_ovarian_validation_july2010'

        if (cached_target_file_url is None):
            if (is_custom == ''):
                if (probe_file_url == 'https://bitbucket.org/cghub/cghub-capture-kit-info/raw/d8b126dd4f33eb7164535e00f0ec9a5985056f34/BI/vendor/Agilent/tcga_6k_genes.baitIntervals.bed'):
                    if (reagent_name == 'Custom V2 Exome Bait, 48 RXN X 16 tubes'):
                        if (reagent_vendor == 'Agilent'):
                            if (target_file_url == 'https://bitbucket.org/cghub/cghub-capture-kit-info/raw/d8b126dd4f33eb7164535e00f0ec9a5985056f34/BI/vendor/Agilent/tcga_6k_genes.targetIntervals.bed'):
                                kit_name = 'tcga_6k_genes'

        if (cached_target_file_url is None):
            if (is_custom == ''):
                if (probe_file_url == 'https://bitbucket.org/cghub/cghub-capture-kit-info/raw/d8b126dd4f33eb7164535e00f0ec9a5985056f34/BI/vendor/Agilent/fhs_jhs_pilot.baitIntervals.bed'):
                    if (reagent_name == 'Custom V2 Exome Bait, 48 RXN X 16 tubes'):
                        if (reagent_vendor == 'Agilent'):
                            if (target_file_url == 'https://bitbucket.org/cghub/cghub-capture-kit-info/raw/d8b126dd4f33eb7164535e00f0ec9a5985056f34/BI/vendor/Agilent/fhs_jhs_pilot.targetIntervals.bed'):
                                kit_name = 'fhs_jhs_pilot'

        # if (cached_target_file_url is None):
        #     if (is_custom == ''):
        #         if (probe_file_url == 'https://bitbucket.org/cghub/cghub-capture-kit-info/raw/d8b126dd4f33eb7164535e00f0ec9a5985056f34/BI/vendor/Agilent/whole_exome_agilent_plus_tcga_6k.baitIntervals.bed'):
        #             if (reagent_name == 'Custom V2 Exome Bait, 48 RXN X 16 tubes'):
        #                 if (reagent_vendor == 'Agilent'):
        #                     if (target_file_url == 'https://bitbucket.org/cghub/cghub-capture-kit-info/raw/d8b126dd4f33eb7164535e00f0ec9a5985056f34/BI/vendor/Agilent/whole_exome_agilent_plus_tcga_6k.targetIntervals.bed'):
        #                         kit_name = ''

        if (cached_target_file_url is None):
            if (is_custom == ''):
                if (probe_file_url == 'https://bitbucket.org/cghub/cghub-capture-kit-info/raw/d8b126dd4f33eb7164535e00f0ec9a5985056f34/BI/vendor/Agilent/cancer_2000gene_shift170.baitIntervals.bed'):
                    if (reagent_name == 'Custom V2 Exome Bait, 48 RXN X 16 tubes'):
                        if (reagent_vendor == 'Agilent'):
                            if (target_file_url == 'https://bitbucket.org/cghub/cghub-capture-kit-info/raw/d8b126dd4f33eb7164535e00f0ec9a5985056f34/BI/vendor/Agilent/cancer_2000gene_shift170.targetIntervals.bed'):
                                kit_name = 'cancer_2000gene_shift170'

        if (cached_target_file_url is None):
            if (is_custom == ''):
                if (probe_file_url == 'https://bitbucket.org/cghub/cghub-capture-kit-info/raw/d8b126dd4f33eb7164535e00f0ec9a5985056f34/BI/vendor/Agilent/whole_exome_unique_gc_sorted.baitIntervals.bed'):
                    if (reagent_name == 'Custom V2 Exome Bait, 48 RXN X 16 tubes'):
                        if (reagent_vendor == 'Agilent'):
                            if (target_file_url == 'https://bitbucket.org/cghub/cghub-capture-kit-info/raw/d8b126dd4f33eb7164535e00f0ec9a5985056f34/BI/vendor/Agilent/whole_exome_unique_gc_sorted.targetIntervals.bed'):
                                kit_name = 'whole_exome_unique_gc_sorted'

        if (cached_target_file_url is None):
            if (is_custom == ''):
                if (probe_file_url == 'https://bitbucket.org/cghub/cghub-capture-kit-info/raw/d8b126dd4f33eb7164535e00f0ec9a5985056f34/BI/vendor/Agilent/whole_exome_agilent_designed_120.baitIntervals.bed'):
                    if (reagent_name == 'Custom V2 Exome Bait, 48 RXN X 16 tubes'):
                        if (reagent_vendor == 'Agilent'):
                            if (target_file_url == 'https://bitbucket.org/cghub/cghub-capture-kit-info/raw/d8b126dd4f33eb7164535e00f0ec9a5985056f34/BI/vendor/Agilent/whole_exome_agilent_designed_120.targetIntervals.bed'):
                                kit_name = 'whole_exome_agilent_designed_120'

        if (cached_target_file_url is None):
            if (is_custom == ''):
                if (probe_file_url == 'https://bitbucket.org/cghub/cghub-capture-kit-info/raw/d8b126dd4f33eb7164535e00f0ec9a5985056f34/BI/vendor/Agilent/whole_exome_refseq_coding.baitIntervals.bed'):
                    if (reagent_name == 'Custom V2 Exome Bait, 48 RXN X 16 tubes'):
                        if (reagent_vendor == 'Agilent'):
                            if (target_file_url == 'https://bitbucket.org/cghub/cghub-capture-kit-info/raw/d8b126dd4f33eb7164535e00f0ec9a5985056f34/BI/vendor/Agilent/whole_exome_refseq_coding.targetIntervals.bed'):
                                kit_name = 'whole_exome_refseq_coding'

        if kit_name is None:
            sys.exit(catalog_number, capture_kit)
        return kit_name

def get_library_kits(library_data, logger):
    capture_kits = library_data.get('capture_kits', list())
    for capture_kit in capture_kits:
        catalog_number = capture_kit.get('catalog_number')
        kit_name = get_capture_kit(capture_kit, logger)
        kit_set.add(kit_name)
    return sorted(list(kit_set))

def get_bam_kits(bam_data, logger):
    bam_keys = sorted(list(bam_data.keys()))
    kit_set = set()
    for bam_key in bam_keys:
        if bam_key == 'target_set' or bam_key == 'center_name':
            continue
        library_name = bam_key
        library_data = bam_data.get(library_name)
        kit_list = get_library_kits(library_data, logger)
        for kit_name in kit_list:
            kit_set.add(kit_name)
    return sorted(list(kit_set))

def get_kits(json_data, bam_name, library_name, logger):
    print(bam_name)
    bam_data = json_data.get(bam_name, list())
    if len(bam_data) == 0:
        return bam_data
    library_data = bam_data.get(library_name, None)
    if library_data is None:
        kit_list = get_bam_kits(bam_data, logger)
    else:
        kit_list = get_library_kits(library_data, logger)
    print(str(kit_list))
    return kit_list
