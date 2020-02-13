<xsl:stylesheet version = '1.0' xmlns:xsl='http://www.w3.org/1999/XSL/Transform'>
 
<xsl:output method="html" encoding="utf-8"/>
<xsl:template match="strings"> 
	<html>
	
	<head>
	<title><xsl:value-of select="@label"/></title>
	<style type="text/css">
		@font-face { font-family: ScheherazadeInst;   src: local(Scheherazade); }
		@font-face { font-family: ScheherazadeTestOTR; src: url(../Scheherazade-R_OTOnly.ttf); }
		@font-face { font-family: ScheherazadeTestOTB; src: url(../Scheherazade-B_OTOnly.ttf); }
		@font-face { font-family: ScheherazadeTestR;  src: url(../Scheherazade-R.ttf); }
		@font-face { font-family: ScheherazadeTestB;  src: url(../Scheherazade-B.ttf); }
		@font-face { font-family: ScheherazadeRefOT;  src: url(../ScheherazadeOT-2.00.ttf); }
		@font-face { font-family: ScheherazadeRef;    src: url(../Scheherazade-2.00.ttf); }
		
		.str    { font-family: "ScheherazadeInst";   font-size: 200%; direction: rtl; text-align: left;}
		.testOTB { font-family: "ScheherazadeTestOTB"; font-size: 200%; direction: rtl; text-align: left;}
		.testR  { font-family: "ScheherazadeTestR";  font-size: 200%; direction: rtl; text-align: left;}
		.testB  { font-family: "ScheherazadeTestB";  font-size: 200%; direction: rtl; text-align: left;}
		.refOT  { font-family: "ScheherazadeRefOT";  font-size: 200%; direction: rtl; text-align: left;}
		.ref    { font-family: "ScheherazadeRef";    font-size: 200%; direction: rtl; text-align: left;}
	</style>
	</head>

	<body>
	<h1><xsl:value-of select="@label"/></h1>
	<table border="1" cellpadding="3" cellspacing="3" style="border-collapse: collapse" bordercolor="#111111">

	<xsl:for-each select="//string">
		  <tr>
		    <td><xsl:value-of select="@label"/></td>
		    <td class="testR">
                <xsl:apply-templates select="." mode="data"/>
		    </td>
		    <td class="testB">
                <xsl:apply-templates select="." mode="data"/>
		    </td>
		    <td class="testOTB">
                <xsl:apply-templates select="." mode="data"/>
		    </td>
<!--
		    <td class="ref">
                <xsl:apply-templates select="." mode="data"/>
		    </td>
-->
<!-- Add column containing feature and lang info -->
		    <td><xsl:value-of select="@lang"/><xsl:text> </xsl:text><xsl:value-of select="@feats"/></td>
<!-- If there is a "text" element, then there may also be a "comment", so put that in the next col -->		    
<xsl:if test="text">
		    <td><xsl:value-of select="comment"/></td>
</xsl:if>
		  </tr>
	</xsl:for-each>

	</table>
	<br/>
	</body>
	
	</html>

</xsl:template>

    <!-- UTILITY FUNCTION to create one data cell -->

    <xsl:template match="*" mode="data">
		<!-- Add style string if there is a feats attribute -->
		<xsl:if test="@feats">
			<xsl:attribute name="style">
				-moz-font-feature-settings: <xsl:value-of select="@feats"/>;
				-ms-font-feature-settings: <xsl:value-of select="@feats"/>;
				-webkit-font-feature-settings: <xsl:value-of select="@feats"/>;
				font-feature-settings: <xsl:value-of select="@feats"/>;
			</xsl:attribute>
		</xsl:if>
		<xsl:if test='@label="Check"'>
			<xsl:attribute name="style">font-size: 150%</xsl:attribute>
		</xsl:if>
		<xsl:if test="@lang">
			<xsl:attribute name="lang"><xsl:value-of select="@lang"/></xsl:attribute>
		</xsl:if>
		<!-- If there is a "text" element then assume the data is there; otherwise the whole node is data -->
		<xsl:choose>
			<xsl:when test="text">
				    	<xsl:value-of select="text"/>
			</xsl:when>
			<xsl:otherwise>
						<xsl:value-of select="."/>
			</xsl:otherwise>
		</xsl:choose>
    </xsl:template>

</xsl:stylesheet>
