# -*- coding: utf-8 -*-
# This file is part of pygal
#
# A python svg graph plotting library
# Copyright © 2012-2014 Kozea
#
# This library is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# This library is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with pygal. If not, see <http://www.gnu.org/licenses/>.

contents = """
{{ id }}.title {
  font-family: monospace;
  font-size: {{ font_sizes.title }};
}

{{ id }}.legends .legend text {
  font-family: monospace;
  font-size: {{ font_sizes.legend }};
}

{{ id }}.axis text {
  font-family: monospace;
  font-size: {{ font_sizes.label }};
}

{{ id }}.axis text.major {
  font-family: monospace;
  font-size: {{ font_sizes.major_label }};
}

{{ id }}.series text {
  font-family: monospace;
  font-size: {{ font_sizes.value }};
}

{{ id }}.tooltip text {
  font-family: monospace;
  font-size: {{ font_sizes.tooltip }};
}

{{ id }}text.no_data {
  font-size: {{ font_sizes.no_data }};
}
"""
