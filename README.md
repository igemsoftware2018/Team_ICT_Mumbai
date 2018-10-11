# Team_ICT_Mumbai
<h1>Hello!</h1>
<h2>About</h2>
BBrickIt is a software that BioBricks any DNA sequence for you.
According to the BioBrick standards, each BioBrick part must have a Prefix and Suffix. [1] In order for a part to be compatible with BioBrick RFC standards, it must not contain the following restriction sites, as these are unique to the prefix and suffix:

<table>
<tr>
<th>Sequence</th>
<th>Type</th>
<th>Enzyme</th>
</tr>
<tr>
<td>gaattc</td>
<td>Illegal</td>
<td>EcoRI</td>
</tr>
<tr>
<td>tctaga</td>
<td>Illegal</td>
<td>XbaI</td>
</tr>
<tr>
<td>actagt</td>
<td>Illegal</td>
<td>SpeI</td>
</tr>
<td>ctgcag</td>
<td>Illegal</td>
<td>PstI</td>
</tr>
<td>gcggccgc</td>
<td>Avoid</td>
<td>NotI</td>
</tr>
<caption> Illegal sites</caption>
</table>

If the sequence to be contains any of these sites, the program will detect them and they will be
highlighted.
The software will also suggest another sequence, with the illegal sequences replaced by new sequences
which do not change the overall amino acid coding sequence.
The most exciting feature of this application is that it takes into account the codon preferences for your
chassis organisms. The frequency and efficiency of usage of codons in different organisms are different
for producing the same amino acid. BBrickIt takes that into account and then suggests a new sequence
that is optimized for the chassis organism.
