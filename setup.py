from setuptools import setup, Command
import pip

# parse_requirements() returns generator of pip.req.InstallRequirement objects
install_reqs = pip.req.parse_requirements("requirements.txt",
                                  session=pip.download.PipSession())

# reqs is a list of requirement
# e.g. ['django==1.5.1', 'mezzanine==1.4.6']
reqs = [str(ir.req) for ir in install_reqs]

setup(
  name='ble',
  version='0.0.1',
  author='Mark Rages',
  author_email='markrages@gmail.com',
  packages=['ble'],
  package_data={'ble':['uuids.json']},
  license=['LICENSE.txt'],
  description=['Python interface to Bluetooth Low Energy devices with BlueZ.'],
  install_requires=reqs,
)
