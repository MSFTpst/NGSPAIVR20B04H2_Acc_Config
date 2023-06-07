from dtaf_core.lib.tklib.infra.bios.bios import BIOS_KNOB_BMC


power_restore_last_bmc = (BIOS_KNOB_BMC(name='AcPwrRcvry'), 'Last')
power_restore_on_bmc = (BIOS_KNOB_BMC(name='AcPwrRcvry'), 'On')

hyper_thread_enabled_bmc = (BIOS_KNOB_BMC(name="MultiThreaded"), "Enabled")
hyper_thread_disabled_bmc = (BIOS_KNOB_BMC(name="MultiThreaded"), "Disabled")

ErrPrompt_default_bmc = (BIOS_KNOB_BMC(name="ErrPrompt"), "Enabled")
ErrPrompt_disabled_bmc = (BIOS_KNOB_BMC(name="ErrPrompt"), "Disabled")

# Mona added for Dell accelerator
ProcX2Apic_enabled_bmc = (BIOS_KNOB_BMC(name="ProcX2Apic"), "Enabled")
ProcX2Apic_disabled_bmc = (BIOS_KNOB_BMC(name="ProcX2Apic"), "Disabled")

DfxDisableBiosDone_disabled_bmc = (BIOS_KNOB_BMC(name="DfxDisableBiosDone"),"Disabled")

# Mona added for Dell accelerator
ProcVirtualization_enabled_bmc = (BIOS_KNOB_BMC(name="ProcVirtualization"),"Enabled")
ProcVirtualization_disabled_bmc = (BIOS_KNOB_BMC(name="ProcVirtualization"),"Disabled")

# Mona added for Dell accelerator SRIOV - Enable_sriov_xmlcli
# Mona captures > knob_setting_sriov_common_xmlcli = (*enable_vtd_xmlcli, *enable_sriov_xmlcli)
# enable_vtd_xmlcli >> ProcX2Apic_enabled_bmc = (BIOS_KNOB_BMC(name="ProcX2Apic"), "Enabled")
# enable_vtd_xmlcli >> ProcVirtualization_enabled_bmc = (BIOS_KNOB_BMC(name="ProcVirtualization"),"Enabled")

SrivoGlobal_enabled_bmc = (BIOS_KNOB_BMC(name="SriovGlobalEnable"),"Enabled")
SrivoGlobal_disabled_bmc = (BIOS_KNOB_BMC(name="SriovGlobalEnable"),"Disabled")

#disable_vtd_bmc = (BIOS_KNOB_BMC ("ProcX2Apic","Disabled","ProcVirtualization","Disabled"))