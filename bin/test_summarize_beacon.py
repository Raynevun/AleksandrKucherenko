import unittest
import imp
beacon = imp.load_source('*', './summarize-beacon')

class TestSummarizeBeacon(unittest.TestCase):

  def test_parse_time(self):
      self.assertTrue("Parsed result timestamp must be more than Epoch time",
                      beacon.parse_time('3 months 1 day 1 hour ago') > 1378395540)


  def test_dict_to_csv(self):
      self.assertEqual(beacon.dict_to_csv({"A":2,"B":3}), "A,2\nB,3")


  def test_count_chars(self):
      self.assertEqual(beacon.count_chars("FDFDEF"), {"F":3,"D":2,"E":1})

  def test_get_output_value(self):
      xml = """<record xmlns="http://beacon.nist.gov/record/0.1/">
                <version>Version 1.0</version>
                <outputValue>12F</outputValue>
                </record>"""
      self.assertEqual(beacon.get_output_value(xml), "12F")


  def test_get_record_xml(self):
      xml = b"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?><record xmlns="http://beacon.nist.gov/record/0.1/"><version>Version 1.0</version><frequency>60</frequency><timeStamp>1378395540</timeStamp><seedValue>87F49DB997D2EED0B4FDD93BAA4CDFCA49095AF98E54B81F2C39B5C4002EC04B8C9E31FA537E64AC35FA2F038AA80730B054CFCF371AB5584CFB4EFD293280EE</seedValue><previousOutputValue>00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000</previousOutputValue><signatureValue>F93BBE5714944F31983AE8187D5D94F87FFEC2F98185F9EB4FE5DB61A9E5119FB0756E9AF4B7112DEBF541E9E53D05346B7358C12FA43A8E0D695BFFAF193B1C3FFC4AE7BCF6651812B6D60190DB8FF23C9364374737F45F1A89F22E1E492B0F373E4DB523274E9D31C86987C64A26F507008828A358B0E166A197D433597480895E9298C60D079673879C3C1AEDA6306C3201991D0A6778B21462BDEBB8D3776CD3D0FA0325AFE99B2D88A7C357E62170320EFB51F9749B5C7B9E7347178AB051BDD097B226664A2D64AF1557BB31540601849F0BE3AAF31D7A25E2B358EEF5A346937ADE34A110722DA8C037F973350B3846DCAB16C9AA125F2027C246FDB3</signatureValue><outputValue>17070B49DBF3BA12BEA427CB6651ECF7860FDC3792268031B77711D63A8610F4CDA551B7FB331103889A62E2CB23C0F85362BBA49B9E0086D1DA0830E4389AB1</outputValue><statusCode>1</statusCode></record>"""
      self.assertEqual(beacon.get_record_xml(1378395540), xml)


if __name__ == '__main__':
    unittest.main()